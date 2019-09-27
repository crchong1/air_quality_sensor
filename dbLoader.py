import pymongo
import csv
import pandas as pd 


# Connect to the MongoDB database we have in the cloud
client = pymongo.MongoClient("mongodb+srv://ewb:ewb@ewb-jtahb.mongodb.net/test?retryWrites=true&w=majority")
db = client.pokemon # we get the pokemon database
collection = db.pokemon_collection # we create a pokemon_collection table
df = pd.read_csv('pokemon.csv') # we read the csv into a pandas dataframe

# print(df.describe) # for describing the data we see

# iterate through all the rows of the csv
for row in df.itertuples():
    # print(row.Name, row.Type1, row.Type2, row.Generation, row.Legendary)
    isLegendary = (row.Legendary == "True")

    # this will be our scheme in the form of a JSON object
    entry = {
        "name": row.Name,
        "type1": row.Type1,
        "type2": row.Type2,
        "generation": row.Generation,
        "isLegendary": isLegendary
    }

    # insert into the collection
    collection.insert_one(entry)

print("Done inserting all data")

# entry = {
#     "name": "name",
#     "type1": "type",
#     "type2": "type2",
#     "generation": "gen",
#     "isLegendary": "isLegendary"
# }

