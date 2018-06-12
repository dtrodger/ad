import json
import unittest

from flask import current_app, url_for
from flask_testing import TestCase

from api.apps import create_app
from api.apps.narcissus.utilities.mock_data import bootstrap_centro_exersize_data, drop_narcissus_collections
from api.apps.narcissus.models.cache.placement import PlacementPeriod
from api.apps.narcissus.middleware.mongo import NarcissusMongo


# TODO - Add docstrings and comments. Test for failures.


class NarcissusEndpointTests(TestCase):

    def create_app(self):
        app = create_app(config='test')
        return app

    def setUp(self):
        self.narcissus_mongo = NarcissusMongo()
        self.narcissus_serializer = PlacementPeriod
        self.headers = {
            'Content-Type': 'application/vnd.api+json',
            'Accept': 'application/vnd.api+json',
            'Authorization': current_app.config['API_TOKEN']
        }
        drop_narcissus_collections()
        bootstrap_centro_exersize_data(self)

    def tearDown(self):
        drop_narcissus_collections()

    def test_get_id_placement(self):
        placement_id = self.placements[0].placement_id
        resp = self.client.get(url_for('narcissus', placement_id=placement_id), headers=self.headers)
        self.assert200(resp)

    def test_get_all_placement(self):
        resp = self.client.get(url_for('narcissus'), headers=self.headers)
        self.assert200(resp)


if __name__ == '__main__':
    unittest.main()