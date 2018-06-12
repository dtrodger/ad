from api.apps.zelos.middleware.mongo import ZelosMongo


def centro_exercise_2a():
    zelos_mongo = ZelosMongo()
    aggr_curs = zelos_mongo.aggr_imprs_costs()
    imprs_costs_strs = zelos_mongo.imps_costs_strs(aggr_curs)

    for imprs_cost_str in imprs_costs_strs:
        print imprs_cost_str
