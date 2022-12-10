"""Flask program example to show a simple configuration."""

import logging
from flask import Flask, request

# Define flask app
app = Flask(__name__)

# Define level of logging and logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# GET method: curl http://localhost:8080/names
@app.route('/names', methods=['GET'])
def get_names():
    """GET method that returns list of names."""
    return names


# POST method: curl -X POST -H "content-Type: application/json"
# -d '{"name": "Carlos"}' http://localhost:8080/add
@app.route('/add', methods=['POST'])
def add_name():
    """POST method that adds a new name into list."""
    name = request.get_json().get('name')

    logger.info("Add new name '%s'", name)
    names.append(name)

    return 'Name added'


# DELETE method: curl -X DELETE -H "content-Type: application/json"
# -d '{"name": "Carlos"}' http://localhost:8080/remove
@app.route('/remove', methods=['DELETE'])
def remove_name():
    """DELETE method that removes a name from the list."""
    name = request.get_json().get('name')

    logger.info("Remove name '%s'", name)
    names.remove(name)

    return 'Name removed'


if __name__ == '__main__':
    names = []
    app.run(host='0.0.0.0', port=8080)
