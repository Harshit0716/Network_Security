import os 
import sys
import json
from dotenv import load_dotenv
load_dotenv()

Mongodb_url=os.getenv("MONGO_DB_URL")
print(Mongodb_url)

import certifi
ca= certifi.where()
import pandas as pd 
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def csv_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            json_data = list(json.loads(df.T.to_json()).values())
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    

    def insert_data_mongodb(self,json_data,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.json_data=json_data

            self.mongo_client=pymongo.MongoClient(Mongodb_url)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.json_data)
            return (len(self.json_data))
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
if __name__ == "__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="NetworkSecurity"
    COLLECTION="phishingData"
    network_data_extract = NetworkDataExtract()
    json_data = network_data_extract.csv_to_json(FILE_PATH)
    print(json_data)
    inserted_count = network_data_extract.insert_data_mongodb(json_data, DATABASE, COLLECTION)
    print(inserted_count)
