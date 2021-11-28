"""import statements"""
from pymongo import MongoClient
import certifi

ca = certifi.where()

#Mongod connection string
url = "mongodb+srv://admin:admin@cluster0.kn0jn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connect to the MongoDB cluster
client = MongoClient(url, tlsCAFile=ca)

# connect pytech database
db = client.pytech

my_col = db.students

my_query = my_col.find({})

for queries in my_query:
    print(my_query)

my_queries = my_col.find_one({"student_id": 1007})
print(my_queries)

#show the connected collections
print(db.list_collection_names)

#show an exit message
input("\n\n End of program, press any key to exit.......")