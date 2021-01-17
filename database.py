import pymongo

from bson.objectid import ObjectId

class Database:
    DB=None

    @staticmethod
    def initialize():
        #client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        client = pymongo.MongoClient('mongodb+srv://richardlin:richardlin@cluster0.4kl8t.azure.mongodb.net/mobile-db?retryWrites=true&w=majority')
        Database.DB = client.mobiledb

    @staticmethod
    def insert_record(doc):
        Database.DB.entries.insert(doc)

    @staticmethod
    def get_records():
        return [x for x in Database.DB.entries.find({})]


    @staticmethod
    def delete_all_records():
        Database.DB.entries.drop()

    @staticmethod
    def delete(id):
        found = Database.DB.entries.find_one({'_id': ObjectId(id)})
        Database.DB.entries.remove(found)
