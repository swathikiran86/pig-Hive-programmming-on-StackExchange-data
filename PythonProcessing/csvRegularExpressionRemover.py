#Import Pandas library for reading and writing CSV
#Import Regular Expressions library
import pandas as pd
import re

#Input the CSV file from the location
df = pd.read_csv("Data/rawCsvData/QueryResults4.csv")

#Using regular expression library remove the HTML tags in both Body and Title columns

df["Body"] = df.Body.apply(lambda b: re.sub('<.*?>','', b))
df["Title"] = df.Title.apply(lambda t: re.sub('<.*?>','', t))

#Removing Commas in Boday,Text and Tags fields
df["Body"] = df.Body.apply(lambda x: re.sub(',*','', x))
df["Title"] = df.Title.apply(lambda y: re.sub(',*','', y))
df["Tags"] = df.Title.apply(lambda y: re.sub(',*','', y))

#Using regular expression library remove the spaces, new lines, tabs in both Body and Title columns
df["Body"] = df.Body.apply(lambda x: re.sub('\\n*\\t*\\r*\\s+',' ', x))
df["Title"] = df.Title.apply(lambda y: re.sub('\\n*\\t*\\r*\\s+',' ', y))

#Writing the data back to CSV files at the Output folder
df.to_csv("Data/processedCsvData/processedQueryResults4.csv")

