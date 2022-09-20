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


starttime = time.time()
print(f'--updateScanPresence.py started: {starttime}--')

active_presence = asoc.getActivePresences()
scanids = asoc.getV1PresenceScans()
for(scans in scanids):
	asoc.updateScanPresence(scan_id,active_presence)
endtime = time.time()
print(f'--updateScanPresence.py ended: {endtime}--')
