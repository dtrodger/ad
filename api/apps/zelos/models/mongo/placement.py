from datetime import datetime

from api.apps.extensions import mongodb


class Delivery(mongodb.EmbeddedDocument):
    date = mongodb.DateTimeField(required=True)
    impressions = mongodb.IntField(required=True)
    embed_dt = mongodb.DateTimeField(default=datetime.now())
    embed_update_dt = mongodb.DateTimeField(default=datetime.now())

    def __repr__(self):
        return '<Delivery: {0}>'.format(self.date)


class PlacementPeriod(mongodb.EmbeddedDocument):
    start = mongodb.DateTimeField(required=True)
    end = mongodb.DateTimeField(required=True)
    cpm = mongodb.IntField(required=True)
    budget = mongodb.IntField(required=True)
    delivery = mongodb.EmbeddedDocumentListField(Delivery)
    embed_dt = mongodb.DateTimeField(default=datetime.now())
    embed_update_dt = mongodb.DateTimeField(default=datetime.now())

    def __repr__(self):
        return '<PlacementPeriod: {0} - {1}>'.format(self.start, self.end)


class Placement(mongodb.Document):
    placement_id = mongodb.IntField(required=True, unique=True)
    name = mongodb.StringField(required=True)
    placement_period = mongodb.EmbeddedDocumentListField(PlacementPeriod)
    created_dt = mongodb.DateTimeField(default=datetime.now())
    updated_dt = mongodb.DateTimeField(default=datetime.now())

    # Allow document to be inherited for dynamic models.
    meta = {
        'allow_inheritance': True,
    }

    def __repr__(self):
        return '<Placement: {0} {1}>'.format(self.placement_id, self.name)