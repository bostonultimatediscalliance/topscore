import base64
import hashlib
import hmac
import requests
import time
import uuid


class TopScoreException(Exception):
    pass


class TopScoreClient(object):
    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url

    def csrf(self):
        nonce = bytes(str(uuid.uuid4()), 'ascii')
        ts = bytes(str(round(time.time())), 'ascii')
        message = bytes(self.client_id, 'ascii') + nonce + ts
        secret = bytes(self.client_secret, 'ascii')
        h = hmac.new(secret, message, digestmod=hashlib.sha256)
        return base64.urlsafe_b64encode(nonce + b'|' + ts + b'|' + base64.urlsafe_b64encode(h.digest()))

    def construct_url(self, endpoint):
        return self.base_url + "/api/" + endpoint

    def get(self, endpoint, page=1, per_page=100, **params):
        params['auth_token'] = self.client_id
        params['api_csrf'] = self.csrf().decode('ascii')
        params['page'] = page
        params['per_page'] = per_page
        return requests.get(self.construct_url(endpoint), params=params)

    def post(self, endpoint, data={}, page=1, per_page=100, **params):
        params['auth_token'] = self.client_id
        params['api_csrf'] = self.csrf().decode('ascii')
        params['page'] = page
        params['per_page'] = per_page
        return requests.post(self.construct_url(endpoint), data=data, params=params)

    def get_paginated(self, endpoint, page=1, per_page=100, **params):
        result = self.get(endpoint, page, per_page, **params).json()
        results = result['result']
        if result['status'] == 200:
            if 'count' in result:
                if result['count'] > (page * per_page):
                    results += self.get_paginated(endpoint, page + 1, per_page, **params)
        else:
            raise TopScoreException("Unable to get a paginated response from TopScore")
        return results

    def get_help(self):
        r = self.get("help")
        return r.json()

    def get_me(self):
        r = self.post("me")
        return r.json()

    def get_events(self, **params):
        return self.get_paginated("events", **params)

    def get_people(self, **params):
        return self.get_paginated("persons", **params)

    def get_person(self, id, **params):
        r = self.get("persons", id=id, **params)
        return r.json()

    def get_tags(self, **params):
        return self.get_paginated("tags", **params)

    def get_tags_show(self, **params):
        r = self.get("tags/show", **params)
        return r.json()

    def get_games(self, **params):
        return self.get_paginated("games", **params)

    def update_game(self, game_id, field, value, **params):
        r = self.post("games/edit", data={
            'game_ids': [game_id],
            'field': field,
            'value': value
        }, **params)
        return r.json()

    def get_games_show(self, **params):
        r = self.get("games/show", **params)
        return r.json()

    def get_teams(self, **params):
        return self.get_paginated("teams", **params)

    def get_fields(self, **params):
        return self.get_paginated("fields", **params)