# MongoDB Exercise Using Restaurant Database
Halo, Assalamu'alaykum.. Hari ini saya akan berbagi tentang hasil latihan access data menggunkan MongoDB. Data yang digunakan adalah:

[data & soal](https://www.w3resource.com/mongodb-exercises/)

Dari 32 soal, baru bisa solve 11 soal. Maklum, newbie. Semoga bermanfaat:

1. Write a MongoDB query to display all the documents in the collection restaurants.

- **Jawaban:**
db.resto.find()

2. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.

- **Jawaban:**
db.resto.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine':1})

3. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.

- **Jawaban:**
db.resto.find({}, {'_id':0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine':1})

4. Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
- **Jawaban:**
db.resto.find({}, {'_id': 0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'address.zipcode':1})

5. Write a MongoDB query to display all the restaurant which is in the borough Bronx.
- **Jawaban:**
db.resto.find({borough:'Bronx'}, {_id:0, name: 1, borough: 1})

6. Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.
- **Jawaban:**
db.resto.find({borough:'Bronx'}, {_id:0, name: 1, borough: 1}).limit(5)

7. Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
- **Jawaban:**
db.resto.find({borough:'Bronx'}, {_id:0, name: 1, borough: 1}).skip(5).limit(5)

8. Write a MongoDB query to find the restaurants who achieved a score more than 90.
- **Jawaban:**
db.resto.find({'grades.score': {$gt: 90}}, {'_id': 0, 'name': 1})

9. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.
- **Jawaban:**
db.resto.find({$and: [{'grades.score': { $gt:80 }}, {'grades.score': { $lt:100 }}]}, {'_id':0, 'name': 1})

10. Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.
- **Jawaban:**
db.resto.find({'address.coord': {$lt: -95.754168}}, {'_id':0, 'name':1})

11. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.
- **Jawaban:**
db.resto.find({$and: [{'cuisine': {$ne: 'Americans'}}, {'grades.score': {$gt: 70}}, {'address.coord': {$lt: -65.754168}}]}, {'_id': 0, 'name': 1})