'''
Created on Dec 12, 2020

@author: EXE2KQF
'''
import json


def data_load():
    with open("contacts.json") as f:
        return json.load(f)

def save_data():
    with open("contacts.json", 'w') as f:
        return json.dump(db,f)

db = data_load()
