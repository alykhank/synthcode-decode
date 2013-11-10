#!usr/bin/env python

import os, json
from pyechonest import track
import requests
from decode import detectKeys
from baseconv import BaseConverter

base27 = BaseConverter('abcdefghijklmnopqrstuvwxyz ')
base13 = BaseConverter('0123456789abc')

if os.environ.get('ID'):
	t = track.track_from_id(os.environ.get('ID'))
else:
	t = track.track_from_filename(os.environ.get('FILE'))
	print 'ID:', t.id

r = requests.get(t.analysis_url).content
segments = json.loads(r)['segments']
print json.dumps(segments, indent=4)

keys = detectKeys(segments)

for idx, k in enumerate(keys):
	if k is 10:
		keys[idx] = 'a'
	elif k is 11:
		keys[idx] = 'b'
	elif k == 12:
		keys[idx] = 'c'
	else:
		keys[idx] = str(k)

print 'Keys:', keys

keyString = ''.join(keys)
keys_10 = base13.decode(keyString)
print 'Base 10:', keys_10
keys_27 = base27.encode(keys_10)
print 'Base 27:', keys_27
