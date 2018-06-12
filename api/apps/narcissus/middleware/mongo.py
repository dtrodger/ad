from api.apps.narcissus.models.mongo.placement import (
    Delivery,
    Placement,
    PlacementPeriod
)
from api.apps.utilities.middleware.mongo.crud import MongoCRUD


class NarcissusMongo(MongoCRUD):
    """
        API to handle CRUD operations against Narcissus MongoEngine models.
    """

    def __init__(self):
        self.delivery = Delivery
        self.placement = Placement
        self.placement_period = PlacementPeriod

    def create_placement(self, placement_id, name, placement_period=None, delivery=None):
        new_placement = self.create(self.placement, placement_id=placement_id, name=name,
                                    placement_period=placement_period, delivery=delivery)

        return new_placement

    def delete_placement(self, placement):
        if isinstance(placement, self.placement):
            return self.delete(placement)
        else:
            raise TypeError('Placement MongoEngine instance required as first arg')

    def get_all_deliveries(self, **kwargs):
        return self.get_all(self.delivery, **kwargs)

    def get_all_placements(self, **kwargs):
        return self.get_all(self.placement, **kwargs)

    def get_all_placement_periods(self, **kwargs):
        return self.get_all(self.placement_period, **kwargs)

    def get_delivery(self, **kwargs):
        return self.get_first(self.delivery, **kwargs)

    def get_placement(self, **kwargs):
        return self.get_first(self.placement, **kwargs)

    def get_placement_period(self, **kwargs):
        return self.get_first(self.placement_period, **kwargs)

    def init_delivery(self, date, impressions):
        new_delivery = self.delivery(date=date, impressions=impressions)

        return new_delivery

    def init_placement_period(self, start, end, cmp, budget):
        new_placement_period = self.placement_period(start=start, end=end, cmp=cmp, budget=budget)

        return new_placement_period

    def update_placement(self, placement, **kwargs):
        if isinstance(placement, self.placement):
            return self.update(placement, **kwargs)
        else:
            raise TypeError('Placement MongoEngine instance required as first arg')
