# CRUD i.e.
CRUD i.e. is a project for implementing a standard crud interface with as many languages and frameworks crosswed with as many data solutions as possible.

## Install
    git clone --recurse-submodules https://github.com/Reggles44/crudie.git
    
## Run
    ./crudie run


# CRUD Structure
The follow Create, Read, Update, and Delete examples are the standard that is implemented in all submodules.

## Create
#### Request
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"foo":"abc","bar": 123}' \
  http://localhost:8000/<language><-framework>/<data_solution>/
```

```
POST /python-fastapi/redis/ HTTP/1.1
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
## Update
## Delete

## Languages, Frameworks, and Datasolutions

|                   | SQL | NoSQL | Redis | Elastic Search |
|-------------------|:---:|:-----:|:-----:|---------------:|
| Python Flask      |     |       |       |                |
| Python Django     |     |       |       |                |
| Python FastAPI    |     |       |       |                |
| GO                |     |       |       |                |
| Rust              |     |       |       |                |


