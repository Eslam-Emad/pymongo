# pymongo
A restful api todoApp using python FastApi and MongoDB

# FastApi
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

 - Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.

 - Fast to code: Increase the speed to develop features by about 200% to 300%. *

 - Fewer bugs: Reduce about 40% of human (developer) induced errors. *

 - Intuitive: Great editor support. Completion everywhere. Less time debugging.

 - Easy: Designed to be easy to use and learn. Less time reading docs.

 - Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.

 - Robust: Get production-ready code. With automatic interactive documentation.

 - Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

* estimation based on tests on an internal development team, building production applications.


## Requirements
 - fastapi
 - pymongo
 - uvicorn
 - starlette
 - pydantic


## Installation
~~~python
$ pip install fastapi
~~~

~~~python
$ pip install uvicorn[standard]
~~~

# MongoDB

About
=====

The PyMongo distribution contains tools for interacting with MongoDB
database from Python.  The ``bson`` package is an implementation of
the `BSON format <http://bsonspec.org>`_ for Python. The ``pymongo``
package is a native Python driver for MongoDB. The ``gridfs`` package
is a `gridfs
<http://www.mongodb.org/display/DOCS/GridFS+Specification>`_
implementation on top of ``pymongo``.

PyMongo supports MongoDB 3.6, 4.0, 4.2, 4.4, and 5.0.


## Installation
~~~python
$ python -m pip install pymongo
~~~

~~~python
$ python -m pip install pymongo[srv]
~~~
