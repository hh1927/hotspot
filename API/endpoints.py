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
@api.route("/cusers/create/<username>")
class cUser(Resource):
    """
    This class supports adding Customer users.
    """

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "A duplicate key")
    # updated parameters of cUser to match workflow
    def post(self, username, age, gender, interests, neighborhood):
        """
        This method creates a new Customer User.
        """
        # database query updated to include fields from parameters
        ret = db.add_cuser(username, age, gender, interests, neighborhood)
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
    def get(self, user_name, party_size):
        # modified parameters & changed function to get
        """
        This method returns all customer users.
        """
        allCusers = db.fetch_cusers()
        if allCusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allCusers


# CHECK api route
@api.route("/busers/create/<username>")
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
    # modified parameters & changed function to get
    def get(self, business_name, age_rest, business_type):
        """
        This method returns all business users.
        """
        allBusers = db.fetch_busers()
        if allBusers is None:
            raise (wz.NotFound("user couldnt be found."))
        else:
            return allBusers


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
    This class supports bUsers inputting
    their daily event information for the cUsers.
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


@api.route("/cDaily")
# added parameters needed for updating customer preferences
class cDaily(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_FOUND, "Not Found")
    def patch(username, new_interests, new_neighborhood, self):
        """
        """
        ret = db.update_cdaily(username, new_interests, new_neighborhood)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("interests not found."))
        else:
            return f"Interest and Neighborhood updated" 

