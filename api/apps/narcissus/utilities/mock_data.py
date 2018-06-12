import datetime
import random

from api.apps.narcissus.middleware.mongo import NarcissusMongo


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

