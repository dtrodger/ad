from api.apps.narcissus.endpoints.resources.placements import PlacementResource


def register_narcissus_endpoints(rest_api):
    """
    Registers Flask-Restful Resource class on Flask-Restful Api instance.

    Argument:
        rest_api (Flask-Restful Api instance)
    """

    rest_api.add_resource(
        PlacementResource,
        '/narcissus/placement',
        '/narcissus/placement/<string:placement_id>',
        endpoint='narcissus'
    )