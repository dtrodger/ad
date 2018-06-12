from api.apps.zelos.middleware.custom_query.aggr import pipeline_imprs_cost
from api.apps.zelos.models.mongo.placement import (
    Delivery,
    Placement,
    PlacementPeriod
)
from api.apps.utilities.middleware.mongo.crud import MongoCRUD


class ZelosMongo(MongoCRUD):
    """
    API to handle CRUD operations against Narcissus MongoEngine models.
    """

    def __init__(self):
        self.delivery = Delivery
        self.placement = Placement
        self.placement_period = PlacementPeriod

    def create_placement(self, placement_id, name, placement_period=None):
        new_placement = self.create(self.placement, placement_id=placement_id, name=name,
                                    placement_period=placement_period)

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

    def init_placement_period(self, start, end, cpm, budget, delivery=None):
        new_placement_period = self.placement_period(start=start, end=end, cpm=cpm, budget=budget, delivery=delivery)

        return new_placement_period

    def update_placement(self, placement, **kwargs):
        if isinstance(placement, self.placement):
            return self.update(placement, **kwargs)
        else:
            raise TypeError('Placement MongoEngine instance required as first arg')

    def aggr_imprs_costs(self):
        aggr_curs = self.placement.objects.aggregate(*pipeline_imprs_cost)

        return aggr_curs

    @staticmethod
    def imps_costs_strs(aggr_curs):
        dt_format = '%m/%d/%Y'
        imprs_cost_strs = []
        for aggr_res in aggr_curs:
            imprs_cost_str = 'Placement {0} ({1}-{2}): {3} impressions @ ${4} CPM = ${5}'.format(
                aggr_res.get('placement_id'),
                aggr_res.get('pp_start').strftime(dt_format),
                aggr_res.get('pp_end').strftime(dt_format),
                '{:,}'.format(aggr_res.get('pp_count_impressions')),
                aggr_res.get('pp_cpm'),
                '{:,.2f}'.format(
                    (aggr_res.get('pp_count_impressions') / 1000.0) * aggr_res.get('pp_cpm')
                )
            )
            imprs_cost_strs.append(imprs_cost_str)

        return imprs_cost_strs
