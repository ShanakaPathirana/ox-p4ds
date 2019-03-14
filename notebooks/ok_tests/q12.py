test = {
  'name': '1.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # 'columns'.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell below Question 1.1 where you defined
          >>> # columns.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'columns' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(columns == ['text', 'to_user_id', 'from_user', 'id', 'from_user_id', 'iso_language_code', 'source', 'profile_image_url', 'geo_type', 'geo_coordinates_0', 'geo_coordinates_1', 'created_at', 'time'])
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
