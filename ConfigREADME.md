The configuration file, tweetmapping.cfg is an INI formatted file for setting various parameters and options for execution of tweet_mapping.py
The options are described below.

*  rest_api_keyfile - specifies the file to look into for the user's NCBO API key.

*  ontologies - a comma separated list of ontology codes used to determine which bioportal ontologies to search. The available codes are in the file ontology_codes.txt

The code is the upper case characters following the last '/' in the URL.  For example the entry for ICD-10 looks like this:

<code>
International Classification of Diseases, Version 10
http://data.bioontology.org/ontologies/ICD10
</code>

The code for this entry is 'ICD10'. 


*  data_path - specify the data directory to look in for the Twitter CSV files.  The format of these files is expected to be in the format output from the project tools. 
Each file must have the headers: 

    <code>firstpost_date,url,trackback_author_nick,content,score,trackback_permalink,trackback_author_url</code>


*  individual_files - if set to 'true' will cause the generation of an individual annotation file for each input file.  
The same path/file name will be used with text '_annotation' appended.  For example the input file Tweets_BleedingDisorders.csv will 
have an annotation file named Tweets_BleedingDisorders.csv_annotation.  If set to anything other than 'true' a single file will be created
containing all annotations.

*  result_file - the file name for all of the annotations.  This is only recommeded for relatively small data sets.




