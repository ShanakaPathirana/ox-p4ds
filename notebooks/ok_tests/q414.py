test = {
  'name': '4.14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't go back and change the input to 1000 
          >>> # rows in order to calculate 'cross_val_scores_1k'.  Check the 
          >>> # instructions after question Q4.13.
          >>> 'cross_val_scores_1k' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(cross_val_scores_1k.mean() < cross_val_scores_100k.mean())
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
