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
import fnmatch
import csv

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
    ont_list = config.get('NCBO','ontologies')

    output = open(config.get('Data','result_file'),'w')
    output.write('trackback_permalink,char_from,char_to,matched,ontology,code,ann_link\n')

    data_loc = config.get('Data','data_path')
    REST_URL = "http://data.bioontology.org"

    individuals = config.get('Data','individual_files').lower()
    if individuals == 'true':
        output.write('Creating single files in the data directory.\n')
    else:
        print 'Writing to: ' + config.get('Data','result_file')


    # Get input tweet information
    matches = []
    for root, dirnames, filenames in os.walk(data_loc):
        for filename in fnmatch.filter(filenames, '*.csv'):
            matches.append(os.path.join(root, filename))

    for csv_file in matches:
        print 'Processing: ', csv_file + '\n\n'

        if individuals == 'true':
            outfile = open(csv_file + '_annotation','w')
            outfile.write('trackback_permalink,char_from,char_to,matched,ontology,code,ann_link\n')

        data = csv.reader(open(csv_file,'rb'), delimiter=',')
        # dump the first row
        data.next()

        for row in data:
            tweet_text = row[3]
            tweet_link = row[5] + ','

            print "Annotating: " + tweet_text + '\n\n'

            # Annotator call
            annotation = get_json(API_KEY, REST_URL + "/annotator?text=" + urllib2.quote(tweet_text)+"&ontologies="+ont_list)

            for n in range(0, len(annotation)):
                char_from = str(annotation[n]['annotations'][0]['from']).strip() + ','
                char_to = str(annotation[n]['annotations'][0]['to']).strip() + ','
                matched = annotation[n]['annotations'][0]['text'] + ','
                ann_link = annotation[n]['annotatedClass']['@id'] + '\n'

                code = (annotation[n]['annotatedClass']['@id'].split('/')[-1]).strip() + ','
                onto = (annotation[n]['annotatedClass']['@id'].split('/')[-2]).strip() + ','

                if individuals == 'true':
                    outfile.write(tweet_link+char_from+char_to+matched+onto+code+ann_link)
                else:
                    output.write(tweet_link+char_from+char_to+matched+onto+code+ann_link)
        if individuals == 'true':
            outfile.close()


    output.close()



if __name__ == "__main__":

    print """
    tweet_mapping.py  Copyright (C) 2014 Timothy W. Cook
    This program comes with ABSOLUTELY NO WARRANTY; for details see README.md.
    This is free software, and you are welcome to redistribute it under certain conditions; see LICENSE for details.

    See ConfigREADME.md for details on usage.
    """

    main()
