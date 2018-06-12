import datetime
import os
import sys
import unittest

from flask_testing import TestCase

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from api.apps import create_app
from api.apps.zelos.models.mongo.placement import (
    Delivery,
    Placement,
    PlacementPeriod
)
from api.apps.zelos.utilities.mock_data import random_placement_period, drop_zelos_collections


# TODO - Add docstrings and comments. Test for failures.


class PlacementMongoTests(TestCase):

    def create_app(self):
        app = create_app(config='test')
        return app

    def setUp(self):
        self.delivery = Delivery
        self.placement = Placement
        self.placement_period = PlacementPeriod

    def tearDown(self):
        drop_zelos_collections()

    def test_init_delivery(self):
        delivery = self.delivery(date=datetime.datetime.now(), impressions=10)
        self.assertIsInstance(delivery, self.delivery)

    def test_init_placement_period(self):
        pp_start, pp_end = random_placement_period()
        deliveries = [self.delivery(date=datetime.datetime.now(), impressions=10)]
        placement_period = self.placement_period(start=pp_start, end=pp_end, cmp=1, budget=1, delivery=deliveries)
        self.assertIsInstance(placement_period, self.placement_period)

    def test_delivery_crud(self):

        # Create
        deliveries = [self.delivery(date=datetime.datetime.now(), impressions=10)]

        pp_start, pp_end = random_placement_period()
        placement_periods = [self.placement_period(start=pp_start, end=pp_end, cmp=1, budget=1, delivery=deliveries)]

        placement = self.placement(placement_id=1, name='Sports', placement_period=placement_periods)
        placement.save()
        self.assertIsInstance(placement, self.placement)

        # Read
        placement_q = self.placement.objects(placement_id=placement.placement_id).first()
        self.assertEquals(placement, placement_q)

        # Update
        placement_q.name = 'Travel'
        placement_q.save()
        self.assertEquals(placement_q.name, 'Travel')

        # Delete
        placement_q_id = placement_q.placement_id
        placement_q.delete()
        self.assertEquals(self.placement.objects(placement_id=placement_q_id).first(), None)



if __name__ == '__main__':
    unittest.main()