pipeline_imprs_cost = [
    {
        '$unwind': '$placement_period'
    },
    {
        '$unwind': '$placement_period.delivery'
    },
    {
        '$group': {
            '_id': {
                'placement_id': '$placement_id',
                'pp_start': '$placement_period.start',
                'pp_end': '$placement_period.end',
                'pp_cpm': '$placement_period.cpm'
            },
            'count': {
                '$sum': '$placement_period.delivery.impressions'
            }
        }
    },
    {
        '$project': {
            '_id': 0,
            'placement_id': '$_id.placement_id',
            'pp_start': '$_id.pp_start',
            'pp_end': '$_id.pp_end',
            'pp_cpm': '$_id.pp_cpm',
            'pp_count_impressions': '$count'
        }
    }
]
