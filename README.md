# TopScore API Client

[TopScore](http://www.usetopscore.com/) provides athletic league and event management for a variety of different sports -- Ultimate Frisbee, Rugby, Handball, and so on.   This is a client for their API.  API documentation can be found in [this Google Doc](https://docs.google.com/document/d/148SFmTpsdon5xoGpAeNCokrpaPKKOSDtrLNBHOIq5c4/edit#), and at https://yoursite.com/api/help.

Lots of functionality isn't supported, because it was written to solve a specific set of problems (specifically for a type of league that is unique to Boston's Ultimate Frisbee scene).  But, the basic structure of the client is straightforward and should be easy enough to extend.

Installation
------------
This library isn't currently available on pypi or anything, so you'll have to install by hand.  To do so:
  1. (optional but recommended) Activate the virtualenv for your use case
  2. At the base level of the library repository, run `python setup.py install`

Examples
--------
### Instantiate a client
```
>>> import topscore
>>> client = topscore.client.TopScoreClient(client_id=TS_CLIENT_ID, client_secret=TS_CLIENT_SECRET, base_url='https://YOURSITE.usetopscore.com')
```

### Get a list of games
```
>>> games = client.get_games(event_id=EVENT_ID)
>>> print(games[0])
{'AwayTeam': {'contact_email': '', 'created_at': '2017-04-22 18:05:07', 'slug': 'shredline-1', 'creator_id': 184880, 'color': None, 'media_item_id': None, 'attendance_window': 4320, 'school_id': None, 'location_id': 452856, 'sport_id': 1, 'images': {'20': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-20-20/uc-logomark-1.png', '200': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-200-200/uc-logomark-1.png', '280': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-280-280/uc-logomark-1.png', '370': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-370-370/uc-logomark-1.png', '40': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-40-40/uc-logomark-1.png'}, 'name': 'SHRedline', 'twitter_name': None, 'updated_at': '2017-04-28 20:37:43', 'date_breakup': None, 'type': None, 'is_event_team': False, 'organization_id': None, 'id': 198130, 'youtube_key': None, 'model': 'team', 'website': '', 'facebook_url': '', 'date_founded': None, 'site_id': 325}, 'start_datetime_tz': '0207-08-15 18:30:00', 'end_time': '20:30:00', 'division_name': 'All Teams', 'is_forfeit': False, 'created_at': '2017-07-11 14:49:45', 'away_game_report_score': None, 'end_date': '0207-08-15', 'stage_name': 'Regular Season', 'status': 'scheduled', 'home_game_report_score': None, 'stage_format': 'pool', 'field_reservation_id': None, 'stage_id': 116729, 'carryover_source_game_id': None, 'home_team_proxy_id': 497163, 'event_name': 'Summer Club League', 'home_team_id': 197972, 'home_team_description': 'Rubs the Duckie', 'field_id': None, 'updated_at': '2017-07-11 14:49:45', 'away_team_id': 198130, 'losing_team_id': None, 'is_locked': False, 'id': 632876, 'field_number': None, 'reported_at': None, 'away_team_description': 'SHRedline', 'end_datetime_tz': '0207-08-15 20:30:00', 'home_score': None, 'model': 'game', 'is_played': False, 'HomeTeam': {'contact_email': '', 'created_at': '2017-04-20 14:16:22', 'slug': 'rubs-the-duckie', 'creator_id': 155605, 'color': None, 'media_item_id': None, 'attendance_window': 4320, 'school_id': None, 'location_id': 469679, 'sport_id': 1, 'images': {'20': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-20-20/uc-logomark-1.png', '200': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-200-200/uc-logomark-1.png', '280': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-280-280/uc-logomark-1.png', '370': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-370-370/uc-logomark-1.png', '40': 'https://d36m266ykvepgv.cloudfront.net/uploads/media/66h47QW8vx/s-40-40/uc-logomark-1.png'}, 'name': 'Rubs the Duckie', 'twitter_name': None, 'updated_at': '2017-06-06 15:53:30', 'date_breakup': None, 'type': None, 'is_event_team': False, 'organization_id': None, 'id': 197972, 'youtube_key': None, 'model': 'team', 'website': '', 'facebook_url': '', 'date_founded': None, 'site_id': 325}, 'away_team_proxy_id': 497164, 'start_date': '0207-08-15', 'away_score': None, 'start_time': '18:30:00', 'winning_team_id': None}
>>> 
```

### Update the start time of a game to 7:00PM
```
>>> client.update_game(GAME_ID, 'start_time', '19:00:00', event_id=EVENT_ID)
```

