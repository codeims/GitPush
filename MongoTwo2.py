import pymongo as pmg

client = pmg.MongoClient("mongodb+srv://codeims:SHUBHAMbabaji056@geekyims.ttwwi0j.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# When we talk about mongo db we can store the data in the form of document like: .json file format
dummy_data = {
    "name": "shubham",
    "mail": "geekyims@gmail.com",
    "subjects": ["data science", "big data", "data analytics"]
}
list_of_records = [
    {'CompanyName': "iNeuron",
     'ProductName': "Affordable",
     'CourseOffered': "FSDS including mock interviews"},

    {'CompanyName': "iNeuron",
     'ProductName': "Affordable",
     'CourseOffered': "FSDS including mock interviews"},

    {'CompanyName': "iNeuron",
     'ProductName': "Affordable",
     'CourseOffered': "FSDS including mock interviews"}
]

database = client['MyInfo']
coll_d = database['MyData']
# coll_d.insert_one(dummy_data)
# coll_d.insert_many(list_of_records)

record = coll_d.find()
for i in record:
    print(i)

