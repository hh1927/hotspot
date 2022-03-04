"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

# from flask import Flask, request, jsonify
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.db as db

# from flask.json import JSONEncoder
# from bson import json_util
# define a cu
# stom encoder point to the json_util provided by pymongo
# (or its dependency bson)
# class CustomJSONEncoder(JSONEncoder):
# def default(self, obj): return json_util.default(obj)

app = Flask(__name__)
api = Api(app)
# app.json_encoder = CustomJSONEncoder


#PATCH
##bQuota
##cDaily

#POST
##eventInfo

# CHECK
@api.route("/endpoints")
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """

    @api.response(HTTPStatus.OK, "Success")
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


# CHECK
@api.route("/cusers/create/<username>")
class cUser(Resource):
    """
    This class supports adding Customer users.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    def post(self, username):
        """
        This method creates a new Customer User.
        """
        ret = db.add_cuser(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db could not be found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable(f"user {username} already exists."))
        return f"{username} added."

        # json_data = request.get_json(force=True)
        # json_data['name'] = username
        # db.add_cuser(json_data)
        # return f"{username} added."


# CHECK
# updated API route
@api.route("/cList")
class cList(Resource):         
    # updated parameters to be in correspondence w workflow
    """
    parameters then used to select consumers
    This class returns a list of all consumer users
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def get(self,user_name, party_size):
        # modified parameters & changed function to get
        """
        This method returns all customer users.
        """
        allCusers = db.fetch_cusers()
        if allCusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allCusers


# CHECK
@api.route("/busers/create/<username>")
class bUser(Resource):
    """
    This class supports business users,
    specifically the users who are hosting events.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    def post(self, username):
        """
        This method creates a new Business User.
        """
        ret = db.add_buser(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db could not be found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable(f"user {username} already exists."))
        return f"{username} added."
        # json_data = request.get_json(force=True)
        # json_data['name'] = username
        # print(json_data)
        # db.add_buser(json_data)
        # return jsonify(json_data)


# CHECK
# updated api route
@api.route("/blist")
class bList(Resource):  
    # updated parameters to be in correspondence to to workflow
    # added additional parameters related to business
    # paramaters then used to select businesses
    """
    This class supports fetching a list of all business users,
    specifically the users who are hosting events.
    """
    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def get(self,business_name, age_rest, business_type):                                             #modified parameters & changed function to get
        """
        This method returns all business users.
        """
        allBusers = db.fetch_busers()
        if allBusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allBusers

# CHECK
@api.route("/clientList")
class cList(Resource):
    """
    This class supports the client List for the Business Users
    Providing a list of clients for that business for specific event,
    including number of total people per party (Party Size)
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def get(self):
        """
        returns the client list for the business user
        """
        allClientList = db.fetch_clientList()
        if allClientList is None:
            raise (wz.NotFound("Client List couldnt be found."))
        else:
            return allClientList

@api.route("/cusers/delete/<username>")
class DeletecUser(Resource):
    """
    This class enables deleting a cuser.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.FORBIDDEN, "A user can only delete themselves.")
    def post(self, username):
        """
        This method deletes a user from the user db.
        """
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Cuser {username} not found."))
        else:
            return f"{username} deleted."


@api.route("/busers/delete/<username>")
class DeletebUser(Resource):
    """
    This class enables deleting a buser.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.FORBIDDEN, "A user can only delete themselves.")
    def post(self, buserName):
        """
        This method deletes a buser from the user db.
        """
        ret = db.del_user(buserName)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"buser {buserName} not found."))
        else:
            return f"{buserName} deleted."


# corrected
@api.route("/cusers/<party>")
class partySize(Resource):
    """
    This class supports consumer users
    telling us their party size
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    def post(self, cusername, party):
        """
        This method tells us party size
        """
        ret = db.add_party(cusername, party)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db could not be found."))
        return f"{party} added."
    
@api.route("/busers/eventInfo")
class eventInfo(Resource):
    """
    This class supports bUsers inputting their daily event information for the cUsers.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    def post(self, eventName, location, price, hours):
        """
        This method creates a new event.
        """
        ret = db.add_event(eventName, location, price, hours)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event doesnt exist yet. Please try again."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable(f"event {eventName} is coming up soon."))
        return f"{eventName} is ready for tonight."

 
@api.route('/busers/delete')
class DeleteEvent(Resource):
    """
    This class enables deleting an event after it occurs
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the admin can delete it.')
    def post(self, eventName, location):
        """
        This method deletes an event from the event db.
        """
        ret = db.del_event(eventName, location)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"{eventName} at {location} not found."))
        else:
            return f"{eventName} has been deleted."
        
@api.route("/bquota")
class bquota(new_quota, Resource): #added parameter needed to update bquota
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def patch(self, new_quota):
        """
        """
        update_quota = db.busers.updateOne({name:business_name},{$set:{quota:new_quota}}) #added line to incorporate updating of business quota 
        allBusers = db.fetch_busers()
        if allBusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allBusers

@api.route("/cDaily")
class cDaily(new_interests, new_neighborhood, Resource): #added parameters needed for updating customer preferences
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def patch(self,new_interests, new_neighborhood):
        """
        """
        update_neighborhood = db.cusers.updateOne({name:user_name},{$set:{neighborhood:new_neighborhood}}) #added line to incorporate updating of users neighborhood 
        update_interests = db.cusers.updateOne({name:user_name},{$set:{interests:new_interests}})          #added line to incorporate updating of users interests        
        if allCusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allCusers

