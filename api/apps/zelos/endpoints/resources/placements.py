from flask_restful import Resource, reqparse, abort
from marshmallow_jsonapi.schema import ValidationError

from api.apps.extensions.cache import flask_cache
from api.apps.zelos.middleware.mongo import ZelosMongo
from api.apps.zelos.models.cache.placement import Placement
from api.apps.utilities.endpoints.req_resp import (
    json_api_resp,
    json_api_not_found_resp,
    authenticate_token,
    parse_json_api_data,
    json_api_success
)


class PlacementResource(Resource):
    method_decorators = [authenticate_token]

    def __init__(self):
        self.zelos_mongo = ZelosMongo()
        self.zelos_serializer = Placement
        self.request_parser = reqparse.RequestParser()
        super(PlacementResource, self).__init__()

    def __repr__(self):
        return '<{0}> Flask-Restful Resource'.format(self.__class__.__name__)

    # @flask_cache.memoize(timeout=50)
    def get(self, placement_id=None):
        """
        Handles HTTP GET requests to /narcissus/placement - /narcissus/placement<string:placement_id>
        """

        # Requsting single resource
        if placement_id:

            # Query Mongo database for Shift
            placement = self.zelos_mongo.get_placement(placement_id=placement_id)

            if placement:
                # Query returned shift. Serialize resource into JSON API specification format.
                resp_json = self.zelos_serializer().dumps(placement).data

                return json_api_resp(resp_json)
            else:
                # Resource not found.
                return json_api_not_found_resp()
        else:
            # Requesting all resources
            # TODO - allowing access to all resources without pageingation can cause a bottleneck.

            # Query Mongo database for all Shifts
            shifts = self.zelos_mongo.get_all_placements()

            if shifts:

                # Query returned shifts. Serialize resource into JSON API specification format.
                resp_json = self.zelos_serializer(many=True).dumps(shifts).data

                return json_api_resp(resp_json)
            else:

                # Resources not found.
                return json_api_not_found_resp()
