import unittest

from flask_testing import TestCase

from api.apps import create_app
from api.apps.narcissus.middleware.mongo import NarcissusMongo
from api.apps.narcissus.utilities.mock_data import drop_narcissus_collections


# TODO - Add docstrings and comments.


class NarcissusMiddlewareMongoTests(TestCase):

    def create_app(self):
        app = create_app(config='test')
        return app

    def setUp(self):
        self.narcissus_mongo = NarcissusMongo()

    def tearDown(self):
        drop_narcissus_collections()


if __name__ == '__main__':
    unittest.main()