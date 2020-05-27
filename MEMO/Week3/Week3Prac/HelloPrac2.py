from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

matrix = db.movies.find_one({'title':'매트릭스'})

matrix_star = matrix['star']

movies = list(db.movies.find({'star':matrix_star}))

db.movies.update_many({'star':matrix_star},{'$set':{'star':0}})