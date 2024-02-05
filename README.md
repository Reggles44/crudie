# CRUD i.e.
CRUD i.e. is a project for implementing a standard crud interface with as many languages (except PHP) and frameworks crosswed with as many data solutions as possible.

|                         | SQL | NoSQL | Redis | Elastic Search |
|-------------------------|:---:|:-----:|:-----:|---------------:|
| Python Flask            |     |       |       |                |
| Python Django           |     |       |       |                |
| Python FastAPI          |     |       |       |                |
| GO                      |     |       |       |                |
| Rust                    |     |       |       |                |
| Ruby on Rails           |     |       |       |                |
| Javascript Express.js   |     |       |       |                |
| Javascript Next.js      |     |       |       |                |
| Javascript NestJS       |     |       |       |                |
| Javascript Meteor.js    |     |       |       |                |
| C# ASP.NET Core         |     |       |       |                |
| Java Spring             |     |       |       |                |

## Install
    git clone --recurse-submodules https://github.com/Reggles44/crudie.git
    
## Run
    ./crudie run


# CRUD Structure
The follow Create, Read, Update, and Delete examples are the standard that is implemented in all submodules.

## Create
#### Request
```
curl -X POST http://localhost:8000/<language><-framework>/<data_solution>/
    -H "Content-Type: application/json"
    -d '{"foo":"abc","bar": 123}'
```

```
POST /python-fastapi/redis/ HTTP/2
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
curl http://localhost:8000/<language><-framework>/<data_solution>/
    -H "Content-Type: application/x-www-form-urlencoded" 
    -d "foo=abc"
```

```
GET /python-fastapi/redis/ HTTP/2
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
curl -X PATCH http://localhost:8000/<language><-framework>/<data_solution>/
    -H "Content-Type: application/json"
    -d '{"foo":"xyz"}'
```

```
PATCH /python-fastapi/redis/ HTTP/2
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
