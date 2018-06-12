import datetime

from api.apps.zelos.middleware.mongo import ZelosMongo


def centro_exercise_2a():
    zelos_mongo = ZelosMongo()
    aggr_curs = zelos_mongo.aggr_imprs_costs()
    imprs_costs = zelos_mongo.imprs_costs_strs(aggr_curs)
    return imprs_costs


def centro_exercise_2b(d_start, d_end):
    zelos_mongo = ZelosMongo()
    aggr_curs = zelos_mongo.aggr_imprs_costs_range(d_start, d_end)
    imprs_cost = zelos_mongo.imprs_costs_range_str(d_start, d_end, aggr_curs)
    return imprs_cost

