from api.apps.zelos.middleware.mongo import ZelosMongo


def centro_exercise_2a():
    zelos_mongo = ZelosMongo()
    imprs_cost_strs = []
    placements = zelos_mongo.get_all_placements()
    for p in placements:
        p_imprs_costs = zelos_mongo.placement_imprs_costs(p.placement_id)
        p_imprs_cost_strs = zelos_mongo.imps_costs_strs(p_imprs_costs)
        imprs_cost_strs.extend(p_imprs_cost_strs)

    for imprs_cost_str in imprs_cost_strs:
        print imprs_cost_str