"""Tornado program example to show a simple configuration."""

import logging
import json
import tornado.web
import tornado.httpserver
import tornado.ioloop

# Define level of logging and logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Just for testing
global names
names = []


class NamesHandler(tornado.web.RequestHandler):
    """Class Handler to control all requests for names."""

    def get(self):
        """GET method that returns list of names."""
        self.write(f"[{','.join(names)}]")

    def post(self):
        """POST method that adds a new name into list."""
        data = json.loads(self.request.body.decode())
        logger.info(data)
        name = data.get('name')
        logger.info("Add new name '%s'", name)
        names.append(name)
        self.write("Name added")

    def delete(self):
        """DELETE method that removes a name from the list."""
        data = json.loads(self.request.body.decode())
        name = data.get('name')
        logger.info("Remove name '%s'", name)
        names.remove(name)
        self.write("Name removed")


app = tornado.web.Application([
    (r"/names", NamesHandler),
])

server = tornado.httpserver.HTTPServer(app)
server.listen(8080)
tornado.ioloop.IOLoop.current().start()
