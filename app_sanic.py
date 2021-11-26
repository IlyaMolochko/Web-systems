from bson import json_util
from database import Database
from sanic import Sanic
from sanic.response import json, text
from sanic.exceptions import NotFound

app = Sanic("Sanic test")
db = Database()

db.connect()


@app.route('/')
async def main_page(request):
    return text('Main page')

@app.route('/tournaments/<tournament_id>')
async def tournament(request, tournament_id):
    result = db.get_tournament(tournament_id)
    if result is None:
        return NotFound('Page not found', status_code=404) 
    return json(json_util.dumps(result))

@app.route('/matches/<match_id>')
async def match(request, match_id):
    result = db.get_match(match_id)
    if result is None:
        return NotFound('Page not found', status_code=404)
    return json(json_util.dumps(result))

if __name__ == '__main__':
    app.run()
