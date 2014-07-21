The configuration file, tweetmapping.cfg is an INI formatted file for setting various parameters and options for execution of tweet_mapping.py
The options are described below.

*  rest_api_keyfile - specifies the file to look into for the user's NCBO API key.

*  data_path - spcify the data directory to look in for the Twitter CSV files.  The format of these files is expected to be in the format output from the project tools. 
Each file must have the headers: 
    <code>firstpost_date,url,trackback_author_nick,content,score,trackback_permalink,trackback_author_url</code>

*  ontologies - a comma separated list of ontology codes used to determine which bioportal ontologies to search. The available codes are in the file ontology_codes.txt
The code is the upper case characters following the last '/' in the URL.  For example the entry for ICD-10 looks like this:
<code>
International Classification of Diseases, Version 10
http://data.bioontology.org/ontologies/ICD10
</code>
The code for this entry is 'ICD10'. 



