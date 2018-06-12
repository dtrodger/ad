import unittest

from flask_testing import TestCase

from api.apps import create_app
from api.apps.zelos.middleware.mongo import ZelosMongo
from api.apps.zelos.utilities.mock_data import drop_zelos_collections


# TODO - Add docstrings and comments.


class ZelosMiddlewareMongoTests(TestCase):

    def create_app(self):
        app = create_app(config='test')
        return app

    def setUp(self):
        self.zelos_mongo = ZelosMongo()

    def tearDown(self):
        drop_zelos_collections()


if __name__ == '__main__':
    unittest.main()