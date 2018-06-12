from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema


class Delivery(Schema):
    id = fields.String(dump_only=True, attribute='placement_id')
    date = fields.DateTime()
    impressions = fields.Int()

    class Meta:
        type_ = 'delivery'


class PlacementPeriod(Schema):
    id = fields.String(dump_only=True, attribute='placement_id')
    start = fields.String()
    end = fields.DateTime()
    cmp = fields.Int()
    delivery = fields.List(fields.Nested(Delivery))
    budget = fields.Int()

    class Meta:
        type_ = 'placement_period'


class Placement(Schema):
    id = fields.String(required=True, dump_only=True, attribute='placement_id')
    name = fields.String()
    placement_period = fields.List(fields.Nested(PlacementPeriod))

    class Meta:
        type_ = 'placement'
        self_view = 'narcissus'
        self_view_many = 'narcissus'
        strict = True