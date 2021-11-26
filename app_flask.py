import json
from bson import json_util
from database import Database
from flask import Flask, jsonify, Response


app = Flask(__name__)
db = Database()

db.connect()

@app.route('/')
def main_page():
    return 'Main page'

@app.route('/tournaments/<tournament_id>', methods=['GET'])
def tournament(tournament_id):
    result = db.get_tournament(tournament_id)
    if result is None:
        return Response('Page not found', status=404) 
    return json.loads(json_util.dumps(result))

@app.route('/matches/<match_id>', methods=['GET'])
def match(match_id):
    result = db.get_match(match_id)
    if result is None:
        return Response('Page not found', status=404) 
    return json.loads(json_util.dumps(result))

if __name__ == '__main__':
    app.run()
