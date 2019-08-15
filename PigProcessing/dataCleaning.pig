
--Loading the data from HDFS location using PigStorage and comma as a delimiter
data = LOAD '/user/pig/processedData/ ' USING PigStorage(',');

--Selecting only required columns amongst total columns and generating column names
requiredFieldsData = FOREACH data GENERATE $0 AS Id:int, $6 AS Score:int, $8 AS Body:chararray, $9 AS OwnerUserId:int, $15 AS Title:chararray, $16 AS Tags:chararray;


--Removing the headers that were in CSV file
headerSkippedData = FILTER requiredFieldsData BY $2 != 'Body';

--Verifying for Null values in OwnerUserID and eliminating those rows
finalData = FILTER headerSkippedData BY (OwnerUserId IS NOT NULL);

--Storing the computed data onto HDFS using PigStorage as comma delimited values.
STORE finalData INTO '/user/pig/cleanedData1' USING PigStorage(',');
