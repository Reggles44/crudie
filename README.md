# CRUD i.e.
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
| Java Springboot         |  .  |       |                |

## TODO LIST
```
Zig
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

Rust: 
    Rewrite querys to return results then parse that for fields


## Install
    git clone --recurse-submodules https://github.com/Reggles44/crudie.git
    
## Run
    ./crudie run


# CRUD Structure
The follow Create, Read, Update, and Delete examples are the standard that is implemented in all submodules.

## Create
#### Request
```
curl -X POST http://localhost:8000/<language><-framework>/<data_solution>/create
    -H "Content-Type: application/json"
    -d '{"foo":"abc","bar": 123}'
```

```
POST /python-fastapi/redis/create HTTP/2
Host: 127.0.0.1
Content-Type: application/json

{
    "foo": "abc",
    "bar": 123
}

```
    
#### Response

```
HTTP/2 201 OK
Content-Type: application/json

{
    "foo": "abc",
    "bar": 123
}
```

## Read
#### Request
```
curl http://localhost:8000/<language><-framework>/<data_solution>/read
    -H "Content-Type: application/x-www-form-urlencoded" 
    -d "foo=abc"
```

```
GET /python-fastapi/redis/read HTTP/2
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded

foo=abc
```
    
#### Response

```
HTTP/2 201 OK
Content-Type: application/json

{
    "foo": "abc",
    "bar": 123
}
```

## Update
#### Request
```
curl -X PATCH http://localhost:8000/<language><-framework>/<data_solution>/update
    -H "Content-Type: application/json"
    -d '{"foo":"xyz"}'
```

```
PATCH /python-fastapi/redis HTTP/2
Host: 127.0.0.1
Content-Type: application/json

{
    "foo": "xyz"
}
```
    
#### Response

```
HTTP/2 200 OK
Content-Type: application/json


{
    "foo": "xyz",
    "bar": 123
}
```

## Delete
#### Request
```
curl -X DELETE http://localhost:8000/<language><-framework>/<data_solution>/
    -H "Content-Type: application/json"
    -d "foo=xyz"
```

```
DELETE /python-fastapi/redis/ HTTP/2
Host: 127.0.0.1
Content-Type: application/json

foo=xyz
```
    
#### Response

```
HTTP/2 200 OK
Content-Type: application/json


{
    "foo": "xyz",
    "bar": 123
}
```
