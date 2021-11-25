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

#student = {
#   "student_id": 10001,
#   "first_name": "Tom",
#   "last_name": "Smith",
#   "semester" : [{
#     "term": "winter",
#     "gpa": "4.1",
#     "start_date": "09/12/2020",
#     "end_date": "05/11/2021",
#     "courses": {
#       "course_id": 1245,
#       "description": "cyber security",
#       "instructor": "Johnson Hendricks",
#       "grade": 91
#     }
#   },
#   {
#     "term": "summer",
#     "gpa" : "4.0",
#     "start_date": "07/05/2021",
#     "end_date": "08/15/2021",
#     "courses": {
#       "course_id": 2345,
#       "description": "web development",
#       "instructor": "William Cranston",
#       "grade": 88
#     }
#   }
#   ]
# }
Fred = {
        "student_id": 1007,
        "first_name": "Fred",
        "last_name": "Mapoly",
        "semester": [{
            "term": "winter",
            "gpa": "3.8",
            "start_date": "09/12/2020",
            "end_date": "05/11/2021",
            "courses": {
                "course_id": 1245,
                "description": "cyber security",
                "instructor": "Johnson Hendricks",
                "grade": 86
            },
        }]
    }

Tony = {
       "student_id": 1008,
       "first_name": "Tony",
       "last_name": "Wallabe",
       "semester": [{
           "term": "winter",
           "gpa": "4.3",
           "start_date": "09/12/2020",
           "end_date": "05/11/2021",
           "courses": {
               "course_id": 1245,
               "description": "cyber security",
               "instructor": "Johnson Hendricks",
               "grade": 94
           }
       }]
   } 
Sammy = {
        "student_id": 1009,
        "first_name": "Sammy",
        "last_name": "Ballpark",
        "semester": [{
            "term": "winter",
            "gpa": "3.0",
            "start_date": "09/12/2020",
            "end_date": "05/11/2021",
            "courses": {
                "course_id": 1245,
                "description": "cyber security",
                "instructor": "Johnson Hendricks",
                "grade": 72
            }
        }]
    }

fred_student = my_col.insert_one(Fred)
tony_student = my_col.insert_one(Tony)
sammy_student = my_col.insert_one(Sammy)


#show the connected collections
print(db.list_collection_names)

#show an exit message
input("\n\n End of program, press any key to exit.......")