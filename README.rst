======================
Fibonacci sequence API
======================
This is a simple implementation of HTTP API on aiohttp.web. Requires Python 3.5+

Usage
-----

``GET {hostname}/v1/fib/{int}`` - get sequnce for a provided integer.
Supports integers in range from 0 to 1000.

Example request:
~~~~~~~~~~~~~~~~
``$ curl http://localhost:8080/v1/fib/10``

Example response:
~~~~~~~~~~~~~~~~~
.. code-block:: json

    {"sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]}

Errors
------
* The number should be in range from 0 to 1000.
* Not an integer.
* Invalid API call.

Implementation / Deployment
---------------------------
Written on aiohttp.web.
Test instance deployed at http://api.s1ck.org:12345 using gunicorn + Nginx.


Author
------

`Alex Sanchez <mailto:alex@s1ck.org>`_.
