#!usr/bin/env python

import os, json
from pyechonest import track
import requests
from decode import detectKeys

if os.environ.get('ID'):
	t = track.track_from_id(os.environ.get('ID'))
else:
	t = track.track_from_filename(os.environ.get('FILE'))
	print 'ID:', t.id

r = requests.get(t.analysis_url).content
segments = json.loads(r)['segments']
print json.dumps(segments, indent=4)

print detectKeys(segments)
