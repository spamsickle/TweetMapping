#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    TweetMapping.py maps twitter healthcare key words to bioportal ontolgies.
    See the README.md file for more information.
    Copyright (C) {2014}  Timothy W. Cook, tim at MLHIM dot Org.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    For more information about our healthcare knowledge modelling work see: http://www.mlhim.org


"""

import urllib2
import json
import os
from pprint import pprint

import ConfigParser, os

def get_json(API_KEY, REST_URL):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(REST_URL).read())

def main():

    # Configuration
    config = ConfigParser.ConfigParser()
    config.readfp(open('tweetmapping.cfg'))
    f = open(config.get('NCBO','rest_api_keyfile'))
    API_KEY = f.readline().strip('\n')
    f.close()
    print config.get('Data','result_file')
    output = open(config.get('Data','result_file'),'w')
    output.write('tweet_link,char_from,char_to,matched,ontology,code,ann_link\n')

    REST_URL = "http://data.bioontology.org"

    # Get input tweet information
    tweet_text = "@subatomicdoc: Tumor HPV status and invasive squamous cell carcinoma of the anus http://t.co/Du8NUMzkLR &gt;@umassmemorial #ASCO14 #ancsm"
    tweet_link = 'http://twitter.com/ABumRap/status/473104369815404544' + ','

    print "Annotating: " + tweet_text + '\n\n'

    # Annotator call
    annotation = get_json(API_KEY, REST_URL + "/annotator?text=" + urllib2.quote(tweet_text)+"&ontologies=ICD10,LOINC,SNOMEDCT")

    for n in range(0, len(annotation)):
        char_from = str(annotation[n]['annotations'][0]['from']) + ','
        char_to = str(annotation[n]['annotations'][0]['to']) + ','
        matched = annotation[n]['annotations'][0]['text'] + ','
        ann_link = annotation[n]['annotatedClass']['@id'] + '\n'

        code = annotation[n]['annotatedClass']['@id'].split('/')[-1] + ','
        onto = annotation[n]['annotatedClass']['@id'].split('/')[-2] + ','

        output.write(tweet_link+char_from+char_to+matched+onto+code+ann_link)
    output.close()



if __name__ == "__main__":

    print """
    tweet_mapping.py  Copyright (C) 2014 Timothy W. Cook
    This program comes with ABSOLUTELY NO WARRANTY; for details see README.md.
    This is free software, and you are welcome to redistribute it under certain conditions; see LICENSE for details.

    See ConfigREADME.md for details on usage.
    """

    main()
