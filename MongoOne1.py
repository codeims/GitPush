import pymongo
client = pymongo.MongoClient("mongodb+srv://codeims:SHUBHAMbabaji056@geekyims.ttwwi0j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "shubham": "paliwal",
    "email": "geekyims@gmail.com",
    "place": "dangarthal"
}

var1 = client['mongotest']
coll = var1['test']
coll.insert_one(d)






