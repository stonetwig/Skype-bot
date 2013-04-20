#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Simple code to answer all the lifes questions by reddit answers!

"""
from __future__ import absolute_import, division, print_function
import sys
import json
import requests

if len(sys.argv) < 2:
    sys.exit("You must ask a question?")

sys.argv.pop(0)
question = ' '.join(sys.argv)

url = 'http://www.reddit.com/r/AskReddit/search.json?q=' + question + '&restrict_sr=on&sort=relevance&t=all'
site = requests.get(url)
data = site.json()
answer = 'I don\'t know the answer to that question :('

try:
	redditquestion = data['data']['children'][0]['data']['id']

	if redditquestion != None or redditquestion != '':
		url = 'http://www.reddit.com/comments/' + redditquestion + '.json?sort=top'
		answer_site = requests.get(url)
		answer_json = answer_site.json()
		for i, rans in enumerate(answer_json[1]['data']['children']):
			ans = rans['data']['body']
			if i == 0:
				continue

			if ans != None and ans != "" and ans != "[deleted]" and len(str(ans)) < 400:
				answer = ans
				break
except:
	True

sys.exit(answer)
