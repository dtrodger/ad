import csv
import datetime
import random
import os
from itertools import ifilter

from flask import current_app

from api.apps.narcissus.middleware.mongo import NarcissusMongo


def bootstrap_centro_exersize_data():
    """
    Mocks Placement MongoEngine models with data from Centro Exersize

    Return:
        placements (list): Placement MongoEngine model instances
    """

    narcissus_mongo = NarcissusMongo()

    # Ensure db empty of Placement documents
    assert not narcissus_mongo.get_all_placements(), 'Clear Narcissus db before bootstraping Centro data'

    def find_existing_placement(p_id):
        """
        Helper function to return existing Placement document from list based on placement_id

        Argument:
            p_id (int): Placement MongoEngine model placement_id attribute

        Return:
            existing_p (Placement)
        """

        existing_p_iter = ifilter(lambda p: p.placement_id == p_id, placements)
        existing_p = next(existing_p_iter)
        return existing_p

    def init_pp_from_csv_row(placement_row):
        """
        Helper to initialize PlacementPeriod embedded documents from csv row

        Argument:
            placement_row (list): row from placements.csv

        Return:
            placement_period (list): list with PlacementPeriod embedded document
        """
        pp_start = datetime.datetime.strptime(placement_row[2], pp_dt_format)
        pp_end = datetime.datetime.strptime(placement_row[3], pp_dt_format)
        pp_cmp = int(placement_row[4])
        pp_budget = int(placement_row[5])

        # Initialize PlacementPeriod embedded document
        placement_period = [narcissus_mongo.init_placement_period(start=pp_start, end=pp_end, cmp=pp_cmp,
                                                                  budget=pp_budget)]

        return placement_period

    # Centro csv placement row date format
    pp_dt_format = '%m/%d/%y'

    # Centro placement csv's path
    placement_path = os.path.abspath(os.path.join(os.getcwd() + '/api/apps/narcissus/utilities/csv/placements.csv'))

    # Save Placement documents from placements.csv
    with current_app.open_resource(placement_path, 'r') as plac_f:

        # Initialize csv reader
        plac_csv = csv.reader(plac_f)
        next(plac_csv)

        placements = []

        # Iterate placements.csv rows
        for placement_row in plac_csv:
            p_id = int(placement_row[0])

            # Placement MongoEngine model with placement_id == current placements.csv row exists
            if p_id in [placement.placement_id for placement in placements]:

                # Init PlacementPeriod model instance and append to existing Placement model placement_period attribute
                placement_period = init_pp_from_csv_row(placement_row)
                existing_p = find_existing_placement(p_id)
                narcissus_mongo.update(existing_p, placement_period=existing_p.placement_period + placement_period)

            else:

                # Init PlacementPeriod model instance and save to new Placement model placement_period attribute
                placement_period = init_pp_from_csv_row(placement_row)
                p_name = placement_row[1]

                placement = narcissus_mongo.create_placement(placement_id=p_id, name=p_name,
                                                             placement_period=placement_period)

                placements.append(placement)

    def init_delviery_from_csv_row(delivery_row):
        """
        Helper to initialize Delivery embedded documents from csv row

        Return:
            delivery (list): list with Delivery embedded document
        """
        d_date = datetime.datetime.strptime(delivery_row[1], d_dt_format)
        d_impressions = int(delivery_row[2])

        # Initialize Delivery embedded document
        delivery = [narcissus_mongo.init_delivery(date=d_date, impressions=d_impressions)]

        return delivery

    # Centro csv delivery row date format
    d_dt_format = '%m/%d/%Y'

    # Centro delivery csv's path
    delivery_path = os.path.abspath(os.path.join(os.getcwd() + '/api/apps/narcissus/utilities/csv/delivery.csv'))

    # Set dict for batch Delivery update
    placement_deliveries = dict()

    with current_app.open_resource(delivery_path, 'r') as del_f:

        # Initialize csv reader
        del_csv = csv.reader(del_f)
        next(del_csv)

        for delivery_row in del_csv:
            delivery = init_delviery_from_csv_row(delivery_row)
            p_id = int(delivery_row[0])

            if p_id in placement_deliveries.keys():
                placement_deliveries[p_id] = placement_deliveries[p_id] + delivery
            else:
                placement_deliveries[p_id] = delivery

    # Batch update Placement documents with Delivery embedded documents
    for placement_id, deliveries in placement_deliveries.iteritems():
        existing_p = find_existing_placement(placement_id)
        narcissus_mongo.update(existing_p, delivery=deliveries)

    # Return newly saved Placement MongeEngine Document model instances
    return placements


def drop_narcissus_collections():
    """
    Drops all Narcissus Mongo collections.
    """

    narcissus_mongo = NarcissusMongo()
    narcissus_mongo.drop_collection(narcissus_mongo.placement)


def random_placement_period():
    """
    Creates random datetime objects.

    Return:
        (datetime, datetime)
    """

    end = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 100))
    start = end - datetime.timedelta(hours=random.randint(1, 8))
    return start, end

