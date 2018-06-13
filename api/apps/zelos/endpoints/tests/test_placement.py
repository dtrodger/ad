import json
import unittest

from flask import current_app, url_for
from flask_testing import TestCase

from api.apps import create_app
from api.apps.zelos.utilities.mock_data import bootstrap_centro_exersize_data, drop_zelos_collections
from api.apps.zelos.middleware.mongo import ZelosMongo


# TODO - Add docstrings and comments. Test for failures.


class ZelosEndpointTests(TestCase):

    def create_app(self):
        app = create_app(config='test')
        return app

    def setUp(self):
        self.zelos_mongo = ZelosMongo()
        self.headers = {
            'Authorization': current_app.config['API_TOKEN']
        }
        drop_zelos_collections()
        bootstrap_centro_exersize_data(self)

    def tearDown(self):
        drop_zelos_collections()

    # def test_get_q_2a(self):
    #     resp = self.client.get(url_for('zelos', q='2a'), headers=self.headers)
    #     self.assert200(resp)
    #
    # def test_get_id_placement(self):
    #     placement_id = self.placements[0].placement_id
    #     resp = self.client.get(url_for('zelos', placement_id=placement_id), headers=self.headers)
    #     self.assert200(resp)

    def test_get_all_placement(self):
        resp = self.client.get(url_for('zelos'), headers=self.headers)
        print resp.data
        self.assert200(resp)


if __name__ == '__main__':
    unittest.main()