import requests
import sys
import json

import cli


class Cache(object):
    def __init__(self, petition_id):
        resp = requests.get('https://petition.parliament.uk/petitions/{}.json'.format(petition_id))
        if resp.status_code != 200:
            try:
                self.json = json.load(open('cache/petition_{}.json'.format(petition_id)))
                return
            except:
                cli.printC("RESPONSE RETURNED BAD RESULT {}".format(resp.status_code), cli.FAIL)
                cli.printC(resp.content, cli.WARNING)
                sys.exit(1)

        self.json = json.loads(resp.content)
        with open("cache/petition_{}.json".format(petition_id), 'w') as f:
            f.write(json.dumps(self.json))

    def get(self):
        return self.json
