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

Ezekiel = {
          "student_id": 1010,
          "first_name": "Ezekiel",
          "last_name": "Taytum",
          "semester": [{
              "term": "winter",
              "gpa": 4.6,
              "start_date": "09/12/2020",
              "end date": "05/11/2021",
              "courses": {
                  "course_id": 1245,
                  "description": "cyber security",
                  "instructor": "Johnson Hendricks",
                  "grade": 96
              }
          }]
}

my_queries = my_col.find({})

for query in my_queries:
    print("First query:", query)

ezekiel_student = my_col.insert_one(Ezekiel)

second_query = my_col.find_one({"student_id": 1010})

print("Student 1010:", second_query) 

final_result = my_col.delete_one({"student_id": 1010})

my_queries = my_col.find({})

for query in my_queries:
    print("Second query:", query)

#show the connected collections
print(db.list_collection_names)

#show an exit message
input("\n\n End of program, press any key to exit.......") 