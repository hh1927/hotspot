"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
#from flask import Flask, request, jsonify
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.db as db

#from flask.json import JSONEncoder

#from bson import json_util

# define a cu
# stom encoder point to the json_util provided by pymongo
# (or its dependency bson)


#class CustomJSONEncoder(JSONEncoder):
#    def default(self, obj): return json_util.default(obj)


app = Flask(__name__)
api = Api(app)
#app.json_encoder = CustomJSONEncoder

#corrected
@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    @api.response(HTTPStatus.OK, 'Success')
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}

#corrected
@api.route('/cusers/create/<username>')
class CreateCuser(Resource):
    """
    This class supports adding Customer users.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        This method creates a new Customer User.
        """
        ret = db.add_cuser(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db could not be found.")
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable(f"user {username} already exists."))
        return f"{username} added."

        '''json_data = request.get_json(force=True)
        json_data['name'] = username
        db.add_cuser(json_data)
        return f"{username} added."''''

#corrected
@api.route('/cusers/all')
class ListCuser(Resource):
    """
    This class returns a list of all consumer users
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        This method returns all customer users.
        """
        allCusers = db.fetch_cusers()
        if allCusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allCusers

#corrected
@api.route('/busers/create/<username>')
class Buser(Resource):
    """
    This class supports business users,
    specifically the users who are hosting events.
    """
    def post(self, username):
        """
        This method creates a new Business User.
        """    
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        This method creates a new Business User.
        """
        ret = db.add_buser(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db could not be found.")
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable(f"user {username} already exists."))
        else:
            raise f"{username} added."
        '''json_data = request.get_json(force=True)
        json_data['name'] = username
        # print(json_data)
        db.add_buser(json_data)
        return jsonify(json_data)'''

#corrected
@api.route('/busers/all')
class ListBuser(Resource):
    """
    This class supports fetching a list of all business users,
    specifically the users who are hosting events.
    """
    def get(self):
        """
        This method returns all business users.
        """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        This method returns all business users.
        """
        allBusers = db.fetch_busers()
        if allBusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allBusers

#corrected
@api.route('/Inv')
class Inv(Resource):
    """
    This class supports fetching a list of all invites,
    from the business including time, place and number of people allowed.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        This method returns all invs.
        """
        allInvs = db.fetch_invs()
        if allInvs is None:
            raise (wz.NotFound("invite couldnt be found."))
        else:
            return allInvs

#corrected
@api.route('/Inv_Response')
class Inv_Response(Resource):
    '''
    This class supports the customer accepting or denying their invite
    from the business
    '''
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        '''
        returns invite responses
        '''
        allInvRes = db.get_inv_response()
        if allInvRes is None:
            raise (wz.NotFound("invite couldnt be found."))
        else:
            return allInvRes

#corrected
@api.route('/clientList')
class ClientList(Resource):
    '''
    This class supports the client List for the Business Users
    Providing a list of clients for that business for specific event,
    including number of total people per party, and time
    '''
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        '''
        returns the client list for the business user
        '''
        allClientList = db.fetch_clientList()
        if allClientList is None:
            raise (wz.NotFound("Client List couldnt be found."))
        else:
            return allClientList

#corrected
@api.route('/clientHist')
class ClientHist(Resource):
    '''
    Gives list of ALL past clients
    for further analytic purposes
    for businesses
    '''
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        '''
        returns the list of prev clients for the business user
        '''
        allClientHist = db.fetch_clientHist()
        if allClientHist is None:
            raise (wz.NotFound("Client is new, without any history."))
        else:
            return allClientHist

#corrected
@api.route('/recList')
class recList(Resource):
    '''
    This class supports the recommendation List of businesses
    for the customers. Providing businesses that they are interested in
    as well as suggestions, given other favorites from customers with
    similar demographics
    '''
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        '''
        returns the recommendation list for the customer user
        '''
        allRecList = db.fetch_recList()
        if allRecList is None:
            raise (wz.NotFound("Rec List couldnt be found."))
        else:
            return allRecList

#corrected
@api.route('/revHist')
class revHist(Resource):
    '''
    Gives list of ALL past reviews
    for further analytic purposes
    for businesses
    '''
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        '''
        returns all reviews the customer user inputted
        '''
        allRevHist = db.fetch_revHist()
        if allRevHist is None:
            raise (wz.NotFound("Review History couldnt be found."))
        else:
            return allRevHist


@api.route('/buser/interest')
class clientsTypes(Resource):
    """
    This class supports fetching the types of clients
    a business user is interested in.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        returns client interests.
        """
        allClientType = db.fetch_clientType()
        if allClientType is None:
            raise (wz.NotFound("Rec List couldnt be found."))
        else:
            return allClientType


@api.route('/buser/promos')
class promos(Resource):
    """
    This class supports fetching that week's promos
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')  
    def get(self):
        """
        returns current promos.
        """
        allPromos = db.fetch_promos()
        if allPromos is None:
            raise (wz.NotFound("Buser has no available promos."))
        else:
            return allPromos


@api.route('/cusers/delete/<username>')
class DeleteCuser(Resource):
    """
    This class enables deleting a cuser.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN, 'A user can only delete themselves.')
    def post(self, username):
        """
        This method deletes a user from the user db.
        """
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Cuser {username} not found."))
        else:
            return f"{username} deleted."
 

@api.route('/busers/delete/<username>')
class DeleteBuser(Resource):
    """
    This class enables deleting a buser.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN, 'A user can only delete themselves.')
    def post(self, username):
        """
        This method deletes a buser from the user db.
        """
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"buser {username} not found."))
        else:
            return f"{username} deleted."
