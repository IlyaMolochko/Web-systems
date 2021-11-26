import pymongo
import pickle
from pymongo import MongoClient

client = MongoClient()
db = client['test']

class Database:
    def __init__(self):
        self.db = None
    
    def connect(self):
        self.db = db
    
    def disconnect(self):
        self.db = None
    
    def get_tournament(self, tournament_id):
        result = self.db['tournaments'].find_one({'tournament_id':tournament_id})
        
        return result
    
    def get_match(self, match_id):
        result = self.db['matches'].find_one({'match_id':match_id})
        
        return result
