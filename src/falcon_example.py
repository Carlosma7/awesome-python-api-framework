"""Falcon program example to show a simple configuration."""

import logging
import falcon

# Define level of logging and logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Just for testing
global names
names = []


class NamesResource:
    """Class Handler to control all requests for names."""

    def on_get(self, req, resp):
        """GET method that returns list of names."""
        resp.body = f"[{','.join(names)}]"
        #self.write(f"[{','.join(names)}]")

    def on_post(self, req, resp):
        """POST method that adds a new name into list."""
        name = req.media.get('name')
        logger.info("Add new name '%s'", name)
        names.append(name)
        resp.body = "Name added"

    def on_delete(self, req, resp):
        """DELETE method that removes a name from the list."""
        name = req.media.get('name')
        logger.info("Remove name '%s'", name)
        names.remove(name)
        resp.body = "Name removed"


api = falcon.API()
api.add_route("/names", NamesResource())
