test = {
  'name': '2.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(predicted_male_height, 2) == 172.37
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(predicted_female_height, 2) == 163.89
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
