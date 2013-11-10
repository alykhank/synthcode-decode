#!usr/bin/env python

import os, json
from pyechonest import track
import requests

if os.environ.get('ID'):
	t = track.track_from_id(os.environ.get('ID'))
else:
	t = track.track_from_filename(os.environ.get('FILE'))
	print 'ID:', t.id
r = requests.get(t.analysis_url).content
segments = json.loads(r)['segments']
print json.dumps(segments, indent=4)
for s in segments:
	print 'Start:', s['start'], 'Duration:', s['duration']
	for idx, p in enumerate(s['pitches']):
		if p == 1.0:
			print 'Key:', idx
