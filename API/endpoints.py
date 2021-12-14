"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
import db.db as db

app = Flask(__name__)
api = Api(app)

'''
@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {'hello': 'world'}
'''


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


@api.route('/cuser')
class Cuser(Resource):
    """
    This class supports fetching a list of all customer users,
    specifically the users who want something to do tonight.
    """
    def get(self):
        """
        This method returns all cusers.
        """
        return db.fetch_cusers()


@api.route('/buser')
class Buser(Resource):
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
    def get(self):
        """
        returns the response for the Invite
        """
        return db.fetch_invRes()


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
        return db.fetch_clientList()
