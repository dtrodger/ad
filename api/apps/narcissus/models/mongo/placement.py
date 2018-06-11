from datetime import datetime

from api.apps.extensions import mongodb


class Delivery(mongodb.EmbeddedDocument):
    date = mongodb.DateTimeField(required=True)
    impressions = mongodb.IntField(required=True)
    embed_dt = mongodb.DateTimeField(default=datetime.now())
    embed_update_dt = mongodb.DateTimeField(default=datetime.now())


class PlacementPeriod(mongodb.EmbeddedDocument):
    start = mongodb.DateTimeField(required=True)
    end = mongodb.DateTimeField(required=True)
    cmp = mongodb.IntField(required=True)
    budget = mongodb.IntField(required=True)
    embed_dt = mongodb.DateTimeField(default=datetime.now())
    embed_update_dt = mongodb.DateTimeField(default=datetime.now())


class Placement(mongodb.Document):
    placement_id = mongodb.IntField(required=True, unique=True)
    name = mongodb.StringField()
    placement_period = mongodb.EmbeddedDocumentListField(PlacementPeriod)
    delivery = mongodb.EmdebbedDocumentListField(Delivery)
    created_dt = mongodb.DateTimeField(default=datetime.now())
    updated_dt = mongodb.DateTimeField(default=datetime.now())

    # Allow document to be inherited for dynamic models.
    meta = {
        'allow_inheritance': True
    }