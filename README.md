# CRUD i.e

CRUD i.e. is a project for implementing a standard crud interface with as many languages (except PHP) and frameworks crosswed with as many data solutions as possible.

<!--toc:start-->
- [CRUD i.e](#crud-ie)
  - [Progress](#progress)
  - [CRUD Structure](#crud-structure)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
<!--toc:end-->

## Progress

|                         | SQL | Redis |
|-------------------------|:---:|:-----:|
|PythonFlask|Tested|Todo|
|PythonDjango|Tested|Todo|
|PythonFastAPI|Tested|Todo|
|GO|Tested|Todo|
|RustActix-Web|Tested|Todo|
|JavaScriptExpress.js|Tested|Todo|
|TypeScriptExpress.js|Tested|Todo|
|JavaSpringboot|Todo|Todo|
|Zig (ZigZag)|Todo|Todo|
|Elixir Phoenix|Todo|Todo|
|Odin|Todo|Todo|
|JS/TS Next.js|Todo|Todo|
|JS/TS NestJS|Todo|Todo|
|JS/TS Meteor.js|Todo|Todo|
|Ocaml|Todo|Todo|
|Haskell|Todo|Todo|
|C++|Todo|Todo|
|C|Todo|Todo|
|COBOL|Todo|Todo|
|Lisp (Hunchentoot)|Todo|Todo|
|C# ASP.NET Core|Todo|Todo|


## CRUD Structure

The follow Create, Read, Update, and Delete examples are the standard that is implemented in all submodules.

### Create

```bash
curl -X POST http://localhost:8000/<app>/create
    -H "Content-Type: application/json"
    -d '{"foo":"abc","bar": 123}'
```

```text
POST /python-fastapi/redis/create HTTP/2
Host: 127.0.0.1
Content-Type: application/json

{
    "foo": "abc",
    "bar": 123
}

```

```text
HTTP/2 201 OK
Content-Type: application/json

{
    "foo": "abc",
    "bar": 123
}
```

### Read

```bash
curl http://localhost:8000/<language><-framework>/<data_solution>/read
    -H "Content-Type: application/x-www-form-urlencoded" 
    -d "foo=abc"
```

```text
GET /python-fastapi/redis/read HTTP/2
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded

foo=abc
```

```text
HTTP/2 201 OK
Content-Type: application/json

{
    "foo": "abc",
    "bar": 123
}
```

### Update

```bash
curl -X PATCH http://localhost:8000/<language><-framework>/<data_solution>/update
    -H "Content-Type: application/json"
    -d '{"foo":"xyz"}'
```

```text
PATCH /python-fastapi/redis HTTP/2
Host: 127.0.0.1
Content-Type: application/json

{
    "foo": "xyz"
}
```

```text
HTTP/2 200 OK
Content-Type: application/json


{
    "foo": "xyz",
    "bar": 123
}
```

### Delete

```bash
curl -X DELETE http://localhost:8000/<language><-framework>/<data_solution>/
    -H "Content-Type: application/json"
    -d "foo=xyz"
```

```text
DELETE /python-fastapi/redis/ HTTP/2
Host: 127.0.0.1
Content-Type: application/json

foo=xyz
```

```text
HTTP/2 200 OK
Content-Type: application/json


{
    "foo": "xyz",
    "bar": 123
}
```
