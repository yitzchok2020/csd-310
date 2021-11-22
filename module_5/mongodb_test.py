"""import statements"""
from pymongo import MongoClient

#Mongod connection string
url = "mongodb+srv://admin:admin@cluster0.kn0jn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connect to the MongoDB cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech

my_col = db.students

student = {
  "student_id": 10001,
  "first_name": "Tom",
  "last_name": "Smith",
  "semester" : [{
    "term": "winter",
    "gpa": "4.1",
    "start_date": "09/12/2020",
    "end_date": "05/11/2021",
    "courses": {
      "course_id": 1245,
      "description": "cyber security",
      "instructor": "Johnson Hendricks",
      "grade": 91
    }
  },
  {
    "term": "summer",
    "gpa" : "4.0",
    "start_date": "07/05/2021",
    "end_date": "08/15/2021",
    "courses": {
      "course_id": 2345,
      "description": "web development",
      "instructor": "William Cranston",
      "grade": 88
    }
  }
  ]
}

addStudent = my_col.insert_one(student)

#show the connected collections
print(db.list_collection_names)

#show an exit message
input("\n\n End of program, press any key to exit.......")