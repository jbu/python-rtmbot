from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import time
import requests
import yaml
import time
import arrow

crontable = [(60, "check_workable")]
outputs = []

workable_token = os.environ['WORKABLE_TOKEN']
base_url = 'https://www.workable.com/spi/v3/accounts/lshift'
headers = {'Content-Type': 'application/json', 
           'Authorization': 'Bearer ' + workable_token}
shortcode = os.environ['WORKABLE_JOB']
last_change = arrow.utcnow().replace(hours=-1)


def check_workable():
	global last_change
	u = '{}/jobs/{}/candidates/?limit=10000'.format(base_url, shortcode)
	r = requests.get(u, headers=headers)
	cl = [c for c in r.json()['candidates'] if arrow.get(c['updated_at']) > last_change]
	last_change = max([arrow.get(c['updated_at']) for c in cl])
	for c in cl:
		t = '{name} updated: {profile_url}'.format(**c)
		outputs.append(["recruitment", t])


def catch_all(data):
    pass
    #if data['channel'].startswith("D"):
    #	print(data)
    #    outputs.append([data['channel'], "from repeat1 \"{}\" in channel {}".format(data['text'], data['channel']) ])

