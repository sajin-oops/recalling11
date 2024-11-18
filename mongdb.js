show databases
use blog
(CRUD OPERATIONS)
CREATE
blog> db.createCollection("users")
{ ok: 1 }

Insert - (insertOne)
blog> db.users.insertOne({ name: "sajin", email: "sajin123@gmail.com", age: 21 })
{
  acknowledged: true,
  insertedId: ObjectId('67155de1ab84a967c8c73bfc')
}

READ - (findOne)
blog> db.users.findOne()
{
  _id: ObjectId('67155de1ab84a967c8c73bfc'),
  name: 'sajin',
  email: 'sajin123@gmail.com',
  age: 21
}
UPDATE -  (updateOne)
blog> db.users.updateOne({name:"sajin"},
... { $set: {age:20}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}

blog> db.users.findOne()
{
  _id: ObjectId('67155de1ab84a967c8c73bfc'),
  name: 'sajin',
  email: 'sajin123@gmail.com',
  age: 20
}
DELETE – (deleteOne)

blog> db.users.deleteOne({
... name:"sajin"})
{ acknowledged: true, deletedCount: 1 }

blog> db.users.findOne()
null
