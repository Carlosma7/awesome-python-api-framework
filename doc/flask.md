# Flask

Table of contents

1. [Introduction](#introduction)
2. [Key Points](#key-points)
2.1. [Pros](#pros)
2.2. [Cons](#cons)
3. [Tutorial](#tutorial)
3.1. [Example](#example)

## Introduction

Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

It does have many cool features like url routing, template engine. It is a WSGI web app framework.

## Key points

### Pros

* **Easy to understand**: Flask let you be in total control in web development taking full creative control of the application and web development. The simplicity of it makes developer able to navigate and create the application easily.
* **Flexible and easy**: Only few parts of flask aren't modifiable because of its minimalism. Flask comes with a template engine that lets you use the same user interface for multiple pages. Almost all parts from flask are open to change.
* **Testing**: Using Flask for web development allows for unit testing through its integrated support, built-in development server, fast debugger, and restful request dispatching.
* **Modularity**: With Flask, you have the ability to create multiple Flask applications or servers, distributed across a large network of servers, each with specific purposes.
* **Performance**: You can think about a micro framework being slightly more “low-level”. There are fewer levels of abstraction between you and the database, the requests, the cache, etc.

### Cons


* **Fewer tools**. You don’t have a full toolset underneath you. So you may need to build more on your own or search out extensions/libraries from the community.
* **Scale**: Another issue about flask is that it has a singular source which means that it will handle every request in turns, one at a time. So if you are trying to serve multiple requests, it will take more time.
* **External modules**. Using more modules is seen as a third party involvement which could be a major breach in security.

## Tutorial

1. Install Flask by running the following command: `pip install Flask`

2. Create a new Python file, and import Flask:

```python
from flask import Flask
```

3. Next, create a new Flask app by calling the Flask constructor and passing in the name of the current module (`__name__`):

```python
app = Flask(__name__)
```

4. Now that you have a Flask app, you can define routes that can be accessed by users. A route is a URL pattern that the Flask app responds to, and a function that is called when that route is accessed. To define a route, use the `@app.route` decorator and specify the URL pattern as the first argument. The function that will be called when that route is accessed is the argument to the decorator. For example:

```python
@app.route('/hello')
def hello():
    return 'Hello, World!'`
```

5. To run the Flask app, call the `run()` method of the Flask app object, and specify the host and port on which the app should run:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

#### Get

In Flask, the `@app.route` decorator is used to bind a function to a specific URL route. This decorator can be used to specify the HTTP methods that the route should respond to, using the `methods` argument. For example, to define a route that only responds to GET requests, you would do the following:

```python
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

```

#### Post

To pass parameters in a POST request in Flask, you can use the `request.form` attribute, which is a dictionary-like object containing the data that was sent in the request body. For example, if you want to pass a name parameter in a POST request and retrieve it in the Flask route, you could do something like this:

```python
@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return f'Hello, {name}!'`
```

Note that you need to import the `request` object from Flask in order to access the `request.form` attribute, like this:

```python
from flask import Flask, request
```

### Example

File is located [here](https://github.com/Carlosma7/awesome-python-api-framework/blob/main/src/flask_example.py).

```python
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
```

Now to test it, you should just execute:

```shell
python3 flask_example.py
```

And you'll see the following (includes info after testing):

![Flask execution](https://github.com/Carlosma7/awesome-python-api-framework/blob/main/img/flask_execution.png)

Now, to test it we will do a small example with:
1. **POST** a new name.
2. **GET** to see list of names.
3. **POST** another name.
4. **GET** to see updated list of names.
5. **DELETE** to remove a name.
6. **GET** to see final list of names.

![Curl requests](https://github.com/Carlosma7/awesome-python-api-framework/blob/main/img/flask_curl.png)
