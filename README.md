# CRUD i.e

CRUD i.e. is a project for implementing a standard crud interface with as many languages (except PHP) and frameworks crosswed with as many data solutions as possible.

|                         | SQL | Redis | Elastic Search |
|-------------------------|:---:|:-----:|---------------:|
| Python Flask            |  .  |       |                |
| Python Django           |  .  |       |                |
| Python FastAPI          |  .  |       |                |
| GO                      |  .  |       |                |
| Rust Actix-Web          |  .  |       |                |
| JavaScript Express.js   |  .  |       |                |
| TypeScript Express.js   |  .  |       |                |
| Java Springboot         |     |       |                |

<!--toc:start-->
- [CRUD i.e](#crud-ie)
  - [TODO LIST](#todo-list)
  - [CRUD Structure](#crud-structure)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
<!--toc:end-->
## TODO LIST

```text
Zig (ZigZag)
Elixir Phoenix
Odin
JS/TS Next.js
JS/TS NestJS
JS/TS Meteor.js
Ocaml
Haskell
C++
C
COBOL
Lisp (Hunchentoot)
C# ASP.NET Core
```

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
