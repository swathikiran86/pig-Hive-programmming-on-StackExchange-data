# pig-Hive-programmming-on-StackExchange-data

Stack Exchange is a network of question and answer websites on diverse topics in many different fields, each site covering a specific topic, where questions, answers, and users are subject to a reputation award process. Using the data from this website, I have performed few tasks to acquire some insights using Pig, Hive and mysql.

Stack Exchange data can be acquired from here:
http://data.stackexchange.com/stackoverflow/query/new


Tasks Performed:

  1. Extracted the data from the StackExchange database using mysql commands
    Acquired the top 200,000 posts by viewcount (see notes on Data Acquisition, you do not need MR/Pig/Hive for this task) 

  2. Using MapReduce/Pig/Hive as required
    Using pig or mapreduce, extracted, transformed and loaded the data as applicable to get : 
      Query 1) The top 10 posts by score
      Query 2) The top 10 users by post score
      Query 3) The number of distinct users, who used the word ‘hadoop’ in one of their posts
      Query 3) Using mapreduce calculate the per-user TF-IDF (just submit the top 10 terms for each of the top 10 users by                    post score, as returned from query 2.)
      
  3. Executed the Pig and Hive tasks on Google Cloud Platform (GCP)
