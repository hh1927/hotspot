"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

# from flask import Flask, request, jsonify
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.data as db

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


# PATCH
# #bQuota
# #cDaily

# POST
# #eventInfo

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


# CHECK api route
@api.route("/cUsers/<username>/<age>//<interests>/<neighborhoods>")
class cUser(Resource):
    """
    This class supports adding Customer users.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    # updated parameters of cUser to match workflow
    def post(self, username, age, interests, neighborhood):
        """
        This method creates a new Customer User.
        """
        # database query updated to include fields from parameters
        ret = db.add_cuser(username, age, interests, neighborhood)
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
@api.route("/cList/<user_name>/<party_size>")
class cList(Resource):
    # updated parameters to be in correspondence w workflow
    """
    parameters then used to select consumers
    This class returns a list of all consumer users
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def get(self, user_name, party_size):
        # modified parameters & changed function to get
        """
        This method returns all customer users.
        """
        update_neighborhood = db.cusers.updateOne({name:user_name},{$set:{neighborhood:new_neighborhood}}) #added line to incorporate updating of users neighborhood 
        update_interests = db.cusers.updateOne({name:user_name},{$set:{interests:new_interests}}) #added line to incorporate updating of users interests 
        allCusers = db.fetch_cusers()        
        if allCusers is None:
            raise (wz.NotFound(f"{user_name} couldnt be found."))
        else:
            return allCusers


# CHECK api route
@api.route("/bUsers/<age_restriction>/<business_name>/<business_type>/<username>/<quota>")
class bUser(Resource):
    """
    This class supports business users,
    specifically the users who are hosting events.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    # updated parameters of bUser to match workflow
    def post(self, username, business_name,
             age_restrictions, business_type, quota):
        """
        This method creates a new Business User.
        """
        # database query updated to include fields from parameters
        ret = db.add_buser(username, business_name,
                           age_restrictions, business_type, quota)
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
@api.route("/bList")
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
    # modified parameters & changed function to get
    def get(self):
        """
        This method returns all business users.
        """
        update_quota = db.busers.updateOne({name:business_name},{$set:{quota:new_quota}}) #added line to incorporate updating of business quota 
        allBusers = db.fetch_busers()
        if allBusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allBusers


@api.route("/cusers/deletecUser/<username>/<age>/<interests>/<neighborhood>")
class deletecUser(Resource):
    """
    This class enables deleting a cuser.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.FORBIDDEN, "A user can only delete themselves.")
    def post(self, username, age, interests, neighborhood):
        """
        This method deletes a user from the user db.
        """
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Cuser {username} not found."))
        else:
            return f"{username} deleted."


@api.route("/busers/deletebUser/<username>")
class deletebUser(Resource):
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
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"buser {username} not found."))
        else:
            return f"{username} deleted."


# corrected
@api.route("/cusers/partySize/<cusername>/<party>")
class partySize(Resource):
    """
    This class supports consumer users
    telling us their party size
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    def post(self, username, party_size):
        """
        This method tells us party size
        """
        ret = db.add_party(username, party_size)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db could not be found."))
        return f"{party} added."


@api.route("/busers/eventInfo/<business_name>/<eventName>/<location>/<price>/<hours>")
class eventInfo(Resource):
    """
    This class supports bUsers inputting
    their daily event information for the cUsers.
    """
    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    def post(self, business_name, eventName, location, price, hours):
        """
        This method creates a new event.
        """
        ret = db.add_event(business_name, eventName, location, price, hours)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event doesnt exist yet. Please try again."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable(f"event {eventName} is coming up soon."))
        return f"{eventName} is ready for tonight."


@api.route('/busers/deleteEvent/<business_name>/<eventName>/<location>/<price>/<hours>')
class deleteEvent(Resource):
    """
    This class enables deleting an event after it occurs
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the admin can delete it.')
    def post(self, business_name, eventName, location, price, hours):
        """
        This method deletes an event from the event db.
        """
        ret = db.del_event(business_name, eventName, location, price, hours)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"{eventName} at {location} not found."))
        else:
            return f"{eventName} has been deleted."


@api.route("/bquota/<username>/<new_quota>")
class bquota(Resource):
    """
    This endpoint will update the value of business quota
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def patch(self, username, new_quota):
        """
        """
        # added line to incorporate updating of business quota
        ret = db.update_bquota(username, new_quota)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Quota not found."))
        else:
            return f"Quota updated to {new_quota}."


@api.route("/cDaily/<username>/<new_interests>/<new_neighborhood>")
# added parameters needed for updating customer preferences
class cDaily(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def patch(self, username, new_interests, new_neighborhood):
        """
        """
        ret = db.update_cdaily(username, new_interests, new_neighborhood)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("interests not found."))
        else:
            return f"{new_interests} and {new_neighborhood} updated"
