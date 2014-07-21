Semantic Mapping of Twitter Healthcare Related Posts to Formal Ontologies
=========================================================================

This repository is to satisfy the research task requirement for the Coursera Data Science, Real World project as defined by the Coursolve need; [Healthcare Twitter Analysis](https://www.coursolve.org/need/184)
This research task will be to explore the possibility and the usefulness of mapping tweet content 
(healthcare keywords) to formal ontologies at the [NCBO Bioportal](http://bioportal.bioontology.org/).

I will develop a Python app to perform the search via REST API and generate a simple ontology to represent the links that can be analyzed and visualized via [Protégé](http://protege.stanford.edu/).
This is where you can find the [Bioportal REST API documentation](http://data.bioontology.org/documentation)

The NCBO REST API examples are included here and modified so that you will place *your* API key in a file named ncbo_api_key.txt 
This file is in the ignore list and will not be upload to GitHub. However, there is an EXAMPLE_ncbo_api_key.txt that shows where to put your api key. You will need to register on the Bioportal to get your own key.  [Documentation for the Bioportal REST API](http://data.bioontology.org/documentation) is on their website. The [wiki](http://www.bioontology.org/wiki/index.php/Main_Page) contains a lot of useful information as well.  I suggest you use these examples to test your API key. They are not needed for the application source tree. 

Usage:
=======


This project requires [Python 2.7](https://docs.python.org/2/) A Python 3.4 version will be available at a later date. 

See the file ConfigREADME.md for details on setting functionality and data paths.  

Once the configuration file is complete just run the executable file:

<code>$./tweetmapping.py</code>

 
 Example:
 --------
 The example data is from the main Google Drive repository labeled as 'June'. 
 These data files are CSV files with headers. The headers are:

 <code>firstpost_date,url,trackback_author_nick,content,score,trackback_permalink,trackback_author_url</code>

 
 
 
 
 
 


