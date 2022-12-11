"""Sanic program example to show a simple configuration."""

import logging
from sanic import Sanic
from sanic.response import json

# Define sanic app
app = Sanic(__name__)

# Define level of logging and logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# GET method: curl http://localhost:8080/names
@app.get('/names')
async def get_names(request):
    """GET method that returns list of names."""
    return json(names)


# POST method: curl -X POST -H "content-Type: application/json"
# -d '{"name": "Carlos"}' http://localhost:8080/add
@app.post('/add')
async def add_name(request):
    """POST method that adds a new name into list."""
    name = request.json.get('name')

    logger.info("Add new name '%s'", name)
    names.append(name)

    return json('Name added')


# DELETE method: curl -X DELETE -H "content-Type: application/json"
# -d '{"name": "Carlos"}' http://localhost:8080/remove
@app.delete('/remove', ignore_body=False)
async def remove_name(request):
    """DELETE method that removes a name from the list."""
    name = request.json.get('name')

    logger.info("Remove name '%s'", name)
    names.remove(name)

    return json('Name removed')


if __name__ == '__main__':
    names = []
    app.run(host='0.0.0.0', port=8080)
