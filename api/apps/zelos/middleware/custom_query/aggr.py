q_pipeline_imprs_cost = [
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
            'count_impressions': {
                '$sum': '$placement_period.delivery.impressions'
            }
        }
    },
    {
        '$sort': {
            '_id.placement_id': 1,
            '_id.pp_start': 1
        }
    },
    {
        '$project': {
            '_id': 0,
            'placement_id': '$_id.placement_id',
            'pp_start': '$_id.pp_start',
            'pp_end': '$_id.pp_end',
            'pp_cpm': '$_id.pp_cpm',
            'pp_count_impressions': '$count_impressions'
        }
    }
]


def q_pipeline_imprs_cost_range_factory(start, end):
    q_pipeline_imprs_cost_range = [
        {
            '$unwind': '$placement_period'
        },
        {
            '$unwind': '$placement_period.delivery'
        },
        {
            '$match': {
                '$and': [
                    {'placement_period.delivery.date': {'$gte': start}},
                    {'placement_period.delivery.date': {'$lte': end}}
                ]
            }
        },
        {
            '$group': {
                '_id': {
                    'placement_id': '$placement_id',
                    'pp_start': '$placement_period.start',
                    'pp_end': '$placement_period.end',
                    'pp_cpm': '$placement_period.cpm'
                },
                'count_impressions': {
                    '$sum': '$placement_period.delivery.impressions'
                }
            }
        },
        {
            '$sort': {
                '_id.placement_id': 1,
                '_id.pp_start': 1
            }
        },
        {
            '$project': {
                '_id': 0,
                'placement_id': '$_id.placement_id',
                'pp_start': '$_id.pp_start',
                'pp_end': '$_id.pp_end',
                'pp_cpm': '$_id.pp_cpm',
                'count_impressions': '$count_impressions'
            }
        }
    ]

    return q_pipeline_imprs_cost_range
