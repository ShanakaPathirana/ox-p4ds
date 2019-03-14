test = {
  'name': '2.10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> number_of_predicted_male_survivors == sample[sample.sex_male == 1].survived.sum()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> number_of_predicted_female_survivors == sample[sample.sex_male == 0].survived.sum()
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