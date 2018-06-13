from api.apps.zelos.endpoints.resources.placements import PlacementResource


def register_zelos_endpoints(rest_api):
    """
    Registers Flask-Restful Resource class on Flask-Restful Api instance.

    Argument:
        rest_api (Flask-Restful Api instance)
    """

    rest_api.add_resource(
        PlacementResource,
        '/zelos/placement',
        '/zelos/placement/<string:placement_id>',
        endpoint='zelos'
    )