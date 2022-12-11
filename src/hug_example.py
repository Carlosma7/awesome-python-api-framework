"""Hug program example to show a simple configuration."""

import logging
import hug

# Define level of logging and logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Just for testing
global names
names = []

# GET method: curl http://localhost:8080/names
@hug.get('/names')
def get_names():
    """GET method that returns list of names."""
    return names


# POST method: curl -X POST -H "content-Type: application/json"
# -d '{"name": "Carlos"}' http://localhost:8080/add
@hug.post('/add')
def add_name(name: hug.types.text):
    """POST method that adds a new name into list."""
    logger.info("Add new name '%s'", name)
    names.append(name)

    return 'Name added'


# DELETE method: curl -X DELETE -H "content-Type: application/json"
# -d '{"name": "Carlos"}' http://localhost:8080/remove
@hug.delete('/remove')
def remove_name(name: hug.types.text):
    """DELETE method that removes a name from the list."""
    logger.info("Remove name '%s'", name)
    names.remove(name)

    return 'Name removed'
