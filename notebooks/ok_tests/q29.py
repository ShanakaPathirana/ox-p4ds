test = {
  'name': '2.9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(incomplete_columns) == set(("age", "fare", "cabin", "embarked", "boat", "body", "home.dest", "age_range"))
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