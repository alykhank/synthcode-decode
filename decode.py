#!usr/bin/env python

import os, json

MIN_DURATION = 0.4
MAX_DURATION = 0.7

def detectKeys(segments):
	timedSegments = []
	smallSegments = []
	for s in segments:
		print 'Duration:', s['duration']
		if len(smallSegments):
			if smallSegments[0]['duration'] + s['duration'] <= MAX_DURATION:
				smallSegments[0]['duration'] += s['duration']
			else:
				for idx, p in enumerate(smallSegments[0]['pitches']):
					if p == 1.0:
						timedSegments.append(idx)
				for idx, p in enumerate(s['pitches']):
					if p == 1.0:
						timedSegments.append(idx)
				del smallSegments[:]
		else:
			if MIN_DURATION <= s['duration']:
				for idx, p in enumerate(s['pitches']):
					if p == 1.0:
						timedSegments.append(idx)
			else:
				smallSegments.append(s)
	return timedSegments

if __name__ == "__main__":
	segments = [
			{
				"confidence": 1.0,
				"timbre": [
					11.472,
					-29.158,
					32.622,
					-144.623,
					128.125,
					54.342,
					10.534,
					-83.214,
					-52.851,
					91.101,
					-35.038,
					10.172
					],
				"pitches": [
					0.01,
					0.01,
					0.009,
					0.013,
					0.007,
					0.008,
					0.008,
					0.009,
					0.01,
					1.0,
					0.022,
					0.018
					],
				"start": 0.0,
				"loudness_max_time": 0.11006,
				"loudness_start": -60.0,
				"duration": 0.89365,
				"loudness_max": -40.819
				},
			{
				"confidence": 0.271,
				"timbre": [
					20.945,
					-162.174,
					52.382,
					-37.967,
					155.203,
					-41.642,
					-34.861,
					-14.725,
					-22.106,
					-0.119,
					4.534,
					-6.731
					],
				"pitches": [
					0.012,
					0.008,
					0.004,
					0.005,
					0.004,
					0.004,
					0.004,
					0.004,
					0.005,
					0.01,
					0.013,
					1.0
					],
				"start": 0.89365,
				"loudness_max_time": 1.00062,
				"loudness_start": -41.52,
				"duration": 1.06821,
				"loudness_max": -36.574
				},
			{
					"confidence": 0.114,
					"timbre": [
						20.34,
						-140.192,
						98.0,
						-9.881,
						175.125,
						-42.358,
						-26.853,
						-4.858,
						-17.36,
						-1.636,
						6.751,
						-21.214
						],
					"pitches": [
						0.019,
						1.0,
						0.024,
						0.008,
						0.007,
						0.008,
						0.006,
						0.007,
						0.006,
						0.011,
						0.009,
						0.018
						],
					"start": 1.96186,
					"loudness_max_time": 0.14755,
					"loudness_start": -41.858,
					"duration": 0.19111,
					"loudness_max": -38.993
					},
			{
					"confidence": 0.239,
					"timbre": [
						22.557,
						-110.92,
						97.533,
						0.451,
						170.464,
						-56.362,
						-39.462,
						-13.845,
						-1.56,
						4.153,
						1.544,
						-7.134
						],
					"pitches": [
						0.015,
						1.0,
						0.034,
						0.013,
						0.009,
						0.006,
						0.007,
						0.006,
						0.007,
						0.006,
						0.006,
						0.007
						],
					"start": 2.15297,
					"loudness_max_time": 0.01289,
					"loudness_start": -39.063,
					"duration": 0.15692,
					"loudness_max": -36.881
					},
			{
					"confidence": 0.328,
					"timbre": [
						24.196,
						-112.127,
						83.546,
						5.764,
						174.612,
						-37.08,
						-27.712,
						-21.671,
						0.23,
						-11.458,
						1.05,
						-12.774
						],
					"pitches": [
						0.017,
						1.0,
						0.033,
						0.008,
						0.005,
						0.004,
						0.006,
						0.004,
						0.005,
						0.007,
						0.008,
						0.006
						],
					"start": 2.30989,
					"loudness_max_time": 0.04276,
					"loudness_start": -37.707,
					"duration": 0.14612,
					"loudness_max": -34.544
					},
			{
					"confidence": 0.362,
					"timbre": [
						25.057,
						-102.957,
						82.411,
						1.42,
						190.047,
						-34.774,
						-26.414,
						-13.473,
						-4.517,
						-34.917,
						-7.49,
						-15.226
						],
					"pitches": [
						0.017,
						1.0,
						0.037,
						0.008,
						0.007,
						0.006,
						0.006,
						0.005,
						0.005,
						0.004,
						0.004,
						0.008
						],
					"start": 2.45601,
					"loudness_max_time": 0.04815,
					"loudness_start": -36.821,
					"duration": 0.13347,
					"loudness_max": -33.014
					},
			{
					"confidence": 0.015,
					"timbre": [
						25.154,
						-112.982,
						85.696,
						-3.872,
						189.235,
						-50.563,
						-26.457,
						-5.521,
						-17.578,
						-16.58,
						5.406,
						-21.438
						],
					"pitches": [
						0.032,
						1.0,
						0.036,
						0.007,
						0.007,
						0.012,
						0.009,
						0.006,
						0.006,
						0.004,
						0.005,
						0.013
						],
					"start": 2.58948,
					"loudness_max_time": 0.04723,
					"loudness_start": -36.614,
					"duration": 0.09197,
					"loudness_max": -34.189
					},
			{
					"confidence": 0.553,
					"timbre": [
						21.849,
						-78.776,
						44.21,
						99.897,
						175.581,
						-31.554,
						-46.6,
						33.28,
						-4.506,
						-23.441,
						-43.09,
						-13.405
						],
					"pitches": [
						0.03,
						0.093,
						1.0,
						0.041,
						0.024,
						0.021,
						0.023,
						0.023,
						0.019,
						0.02,
						0.024,
						0.025
						],
					"loudness_end": -54.947,
					"start": 2.68145,
					"loudness_max_time": 0.08242,
					"loudness_start": -35.044,
					"duration": 1.77633,
					"loudness_max": -29.177
					}
			]
	print detectKeys(segments)
