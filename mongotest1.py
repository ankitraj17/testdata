import pymongo
client = pymongo.MongoClient("mongodb+srv://ankit17jan:Akku9334%40@cluster0.xqk9e.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"ankit",
    "email":"ankit@gmail.com",


}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)