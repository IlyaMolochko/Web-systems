import json
from bson import json_util
from database import Database

from fastapi import FastAPI


app = FastAPI()
db = Database()

db.connect()

@app.get('/')
def main_page():
    return 'Main page'

@app.get('/tournaments/{tournament_id}')
async def tournament(tournament_id):
    result = db.get_tournament(tournament_id)
#     if result is None:
#         return Response('Page not found', status=404) 
    return json.loads(json_util.dumps(result))

@app.route('/matches/{match_id}')
async def match(match_id):
    result = db.get_match(match_id)
#     if result is None:
#         return Response('Page not found', status=404) 
    return json.loads(json_util.dumps(result))

# if __name__ == '__main__':
#     app.run()
