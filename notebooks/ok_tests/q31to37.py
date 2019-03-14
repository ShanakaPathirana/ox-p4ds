test = {
  'name': '3.1-3.7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_product_items_in_dataset == 169
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> num_transactions_in_dataset == 9835
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dataset_density == 0.02609
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> most_common_5_items == ['whole milk', 'other vegetables', 'rolls/buns', 'soda', 'yogurt']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_transactions_containing_soda == 1715
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_transactions_containing_1_item == 2159
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max_num_product_items_in_a_transcation == 32
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
