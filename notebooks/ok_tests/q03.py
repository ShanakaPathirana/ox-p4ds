test = {
  'name': '0.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # 'abba_names'.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell below Question 0.3 where you defined
          >>> # abba_names.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'abba_names' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(abba_names) == set(["Björn", "Benny", "Agnetha", "Anni-Frid"])
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
