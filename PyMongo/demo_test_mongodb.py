# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:43:19 2020

@author: Minzel
"""

import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test_gg_db']
collection_currency = db['PAP_addr']

with open('improved_data.json') as f:
    file_data = json.load(f)

# if pymongo < 3.0, use insert()
#collection_currency.insert(file_data)
# if pymongo >= 3.0 use insert_one() for inserting one document
collection_currency.insert_one(file_data)
# if pymongo >= 3.0 use insert_many() for inserting many documents
#collection_currency.insert_many(file_data)

client.close()