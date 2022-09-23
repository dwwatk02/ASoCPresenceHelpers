#!/usr/bin/env python3

from asoc_api import ASoC
import urllib3
import json
import time

urllib3.disable_warnings()

#API Key
keyId=""
keySecret=""

asoc = ASoC(keyId, keySecret)

code, result = asoc.login()
if code != 200:
	print(f'error logging into ASOC!! code is {code}')

active_presence = sys.argv[1]

## uncomment the following two lines and comment the preceding line to use the first V2 presence ID fetched via API instead of the user-inputted presence ID
#active_presence_dict = asoc.getActivePresences()
#active_presence = active_presence_dict[0]['Id']

scanids = asoc.getV1PresenceScans()

for scans in scanids:
	scan = scans['Id']
	asoc.updateScanPresence(scans,active_presence)

