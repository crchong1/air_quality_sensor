import pymongo
import csv
import pandas as pd 
import numpy as np 

client = pymongo.MongoClient("mongodb+srv://ewb:ewb@ewb-jtahb.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
df = pd.read_csv('pokemon.csv')
print(df.describe)

for row in df.head().itertuples():
    print(row.Name, row.Type1, row.Type2, row.Generation, row.Legendary)
    
# entry = {
#     "name": "name",
#     "type1": "type",
#     "type2": "type2",
#     "generation": "gen",
#     "isLegendary": "isLegendary"
# }

