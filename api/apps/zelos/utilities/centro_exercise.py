import datetime

from api.apps.zelos.middleware.mongo import ZelosMongo


def centro_exercise_2a():
    zelos_mongo = ZelosMongo()
    aggr_curs = zelos_mongo.aggr_imprs_costs()
    imprs_costs = zelos_mongo.imprs_costs_strs(aggr_curs)
    return imprs_costs


def centro_exercise_2b(d_start, d_end):
    dt_format = '%m/%d/%Y'
    if isinstance(d_start, unicode):
        try:
            d_start = datetime.datetime.strptime(d_start, dt_format)
        except Exception as e:
            print ('Start datetime format MM/DD/YYYY required')
            return None

    if isinstance(d_end, unicode):
        try:
            d_end = datetime.datetime.strptime(d_end, dt_format)
        except Exception as e:
            print ('End datetime format MM/DD/YYYY required')
            return None

    zelos_mongo = ZelosMongo()
    aggr_curs = zelos_mongo.aggr_imprs_costs_range(d_start, d_end)
    imprs_cost = zelos_mongo.imprs_costs_range_str(d_start, d_end, aggr_curs)
    return imprs_cost

