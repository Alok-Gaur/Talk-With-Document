from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import config

def get_db():
    client = MongoClient(config.DB_URI, server_api = ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You are successfully connected to Database.")
        
        if not config.DB_NAME:
            raise ValueError("DB_NAME is not set in the environment variables.")
        db = client[config.DB_NAME]
        return db
    except Exception as e:
        print(e)

def store_document(db, collection_name, document):
    if not db:
        raise ValueError("Database connection is not established.")
    if not collection_name:
        raise ValueError("Collection name must be provided.")
    collection = db[collection_name]
    result = collection.insert_one(document)


def get_collection(db, collection_name, embeddings, top_k=3):
    if not db:
        raise ValueError("Database connection is not established.")
    if not collection_name:
        raise ValueError("Collection name must be provided.")
    if not embeddings:
        raise ValueError("Embeddings must be provided.")
    if not isinstance(top_k, int) or top_k <= 0:
        raise ValueError("top_k must be a positive integer.")
    collection = db[collection_name]
    results = collection.find().sort("embedding", -1).limit(top_k)
    return list(results)
    