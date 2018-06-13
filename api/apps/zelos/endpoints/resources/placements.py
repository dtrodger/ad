from flask_restful import Resource, reqparse, abort
from marshmallow_jsonapi.schema import ValidationError

from api.apps.extensions.cache import flask_cache
from api.apps.zelos.middleware.mongo import ZelosMongo
from api.apps.zelos.models.cache.placement import Placement
from api.apps.utilities.endpoints.req_resp import (
    json_api_resp,
    json_api_not_found_resp,
    json_api_success,
    authenticate_token
)
from api.apps.zelos.utilities.centro_exercise import centro_exercise_2a


class PlacementResource(Resource):
    method_decorators = [authenticate_token]

    def __init__(self):
        self.zelos_mongo = ZelosMongo()
        self.zelos_serializer = Placement
        self.request_parser = reqparse.RequestParser
        super(PlacementResource, self).__init__()

    def __repr__(self):
        return '<{0}> Flask-Restful Resource'.format(self.__class__.__name__)

    # @flask_cache.memoize(timeout=50)
    def get(self, placement_id=None):
        """
        Handles HTTP GET requests to /narcissus/placement - /narcissus/placement/<string:placement_id>
        """

        req_args = self.parse_get()

        if placement_id:
            self.query_resource(placement_id)
        elif req_args.get('q'):
            return getattr(self, 'query_{0}'.format(req_args['q']))()
        else:
            self.query_resource_all()

    def query_resource(self, placement_id):
        # Query Mongo database for Shift
        placement = self.zelos_mongo.get_placement(placement_id=placement_id)

        if placement:
            # Query returned shift. Serialize resource into JSON API specification format.
            resp_json = self.zelos_serializer().dumps(placement).data

            return json_api_resp(resp_json)
        else:
            # Resource not found.
            return json_api_not_found_resp()

    def query_resource_all(self):
        # Requesting all resources
        # TODO - allowing access to all resources without pageingation can cause a bottleneck.

        # Query Mongo database for all Placements
        placements = self.zelos_mongo.get_all_placements()

        if placements:
            # Query returned shifts. Serialize resource into JSON API specification format
            resp_json = self.zelos_serializer(many=True).dumps(placements).data

            return json_api_resp(resp_json)
        else:

            # Resources not found.
            return json_api_not_found_resp()

    @staticmethod
    def query_2a():
        imprs_costs = centro_exercise_2a()

        if imprs_costs:
            return json_api_success(imprs_costs)
        else:
            return json_api_not_found_resp()

    def parse_get(self):
        parser = self.request_parser()
        parser.add_argument('q', type=str, choices=('2a'), help="'query' accepted values ('2a')", default=None,
                            required=False)
        args = parser.parse_args()
        return args
