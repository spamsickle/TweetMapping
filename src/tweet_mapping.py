#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    TweetMapping.py maps twitter healthcare key words to bioportal ontolgies.
    See the README.md file for more inforamtion.
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
import ConfigParser, os

def main():
    config = ConfigParser.ConfigParser()
    config.readfp(open('tweetmapping.cfg'))
    print(config.get('NCBO','rest_api_keyfile'))


if __name__ == "__main__":

    print """
    tweet_mapping.py  Copyright (C) 2014 Timothy W. Cook
    This program comes with ABSOLUTELY NO WARRANTY; for details see README.md.
    This is free software, and you are welcome to redistribute it under certain conditions; see LICENSE for details.

    See ConfigREADME.md for details on usage.
    """

    main()
