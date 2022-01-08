"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
# import json
from flask import Flask, request, jsonify
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.db as db
# import werkzeug.exceptions as wz

from flask.json import JSONEncoder

from bson import json_util

# define a cu
# stom encoder point to the json_util provided by pymongo
# (or its dependency bson)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj): return json_util.default(obj)


app = Flask(__name__)
api = Api(app)
app.json_encoder = CustomJSONEncoder


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


'''
@api.route('/pets') #Example of an Endpoint
class Pets(Resource):
    """
    This class supports fetching a list of all pets.
    """
    def get(self):
        """
        This method returns all pets.
        """
        return db.fetch_pets()
'''


@api.route('/users/create/<username>')
class CreateCuser(Resource):
    """
    This class supports adding Customer users.
    """

    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        This method adds a customer user.
        """
        json_data = request.get_json(force=True)
        json_data['name'] = username
        db.add_cuser(json_data)
        return f"{username} added."


@api.route('/cusers/all')
class GetCuser(Resource):
    """
    This class supports fetching a list of all consumer users
    """
    def get(self):
        """
        This method returns all busers.
        """
        return db.fetch_cusers()


@api.route('/busers/create/<username>')
class Buser(Resource):
    """
    This class supports business users,
    specifically the users who are hosting events.
    """
    def post(self, username):
        """
        This method adds a Business User.
        """
        json_data = request.get_json(force=True)
        json_data['name'] = username
        # print(json_data)
        db.add_buser(json_data)
        return jsonify(json_data)


@api.route('/busers/all')
class GetBuser(Resource):
    """
    This class supports fetching a list of all business users,
    specifically the users who are hosting events.
    """
    def get(self):
        """
        This method returns all busers.
        """
        return db.fetch_busers()


@api.route('/Inv')
class Inv(Resource):
    """
    This class supports fetching a list of all invites,
    from the business including time, place and number of people allowed.
    """
    def get(self):
        """
        This method returns all invs.
        """
        return db.fetch_invs()


@api.route('/Inv_Response')
class Inv_Response(Resource):
    '''
    This class supports the customer accepting or denying their invite
    from the business
    '''

    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        returns the response for the Invite
        """
        ret = db.add_inv_response(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("User name already exists."))
        return f"{username} added."


@api.route('/clientList')
class ClientList(Resource):
    '''
    This class supports the client List for the Business Users
    Providing a list of clients for that business for specific event,
    including number of total people per party, and time
    '''
    def get(self):
        '''
        returns the client list for the business user
        '''
        return db.fetch_clientList()


@api.route('/clientHist')
class ClientHist(Resource):
    '''
    Gives list of ALL past clients
    for further analytic purposes
    for businesses
    '''
    def get(self):
        '''
        returns the list of prev clients for the business user
        '''
        return db.fetch_clientHist()


@api.route('/recList')
class recList(Resource):
    '''
    This class supports the recommendation List of businesses
    for the customers. Providing businesses that they are interested in
    as well as suggestions, given other favorites from customers with
    similar demographics
    '''
    def get(self):
        '''
        returns the recommendation list for the customer user
        '''
        return db.fetch_recList()


@api.route('/revHist')
class revHist(Resource):
    '''
    Gives list of ALL past reviews
    for further analytic purposes
    for businesses
    '''
    def get(self):
        '''
        returns all reviews the customer user inputted
        '''
        return db.fetch_revHist()


@api.route('/buser/interest')
class clientsTypes(Resource):
    """
    This class supports fetching the types of clients
    a business user is interested in.
    """
    def get(self):
        """
        returns client categories of interest.
        """
        return db.fetch_clientType()


@api.route('/buser/promos')
class promos(Resource):
    """
    This class supports fetching that week's promos
    """
    def get(self):
        """
        returns current promos.
        """
        return db.fetch_promos()
