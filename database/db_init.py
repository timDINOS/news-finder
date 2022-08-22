from pymongo import MongoClient

username = "timchoi"

password = "Nbafinals123"

connection = MongoClient("mongodb+srv://{username}:{password}@newscluster.v3omj8w.mongodb.net/?retryWrites=true&w=majority")

newsDB = connection["news"]

accounts = newsDB["accounts"]


