import json
import requests
import time

time.sleep(1)

healthy = False
timeout = 5
count = 0
while not healthy:
    health_check = requests.request(method="GET", url="http://localhost:8888")
    healthy = health_check.ok
    count += 1
    if count >= timeout:
        health_check.raise_for_status()


create = requests.request(
    method="POST", url="http://localhost:8888/create", json={"foo": "abc", "bar": 123}
)
create.raise_for_status()
print(json.dumps(create.json(), indent=4, default=str))
id = create.json()["id"]


read = requests.request(method="GET", url=f"http://localhost:8888/read/{id}")
read.raise_for_status()
print(json.dumps(read.json(), indent=4, default=str))


update = requests.request(
    method="PATCH",
    url=f"http://localhost:8888/update/{id}",
    json={"foo": "xyz", "bar": 890},
)
update.raise_for_status()
print(json.dumps(update.json(), indent=4, default=str))


delete = requests.request(method="DELETE", url=f"http://localhost:8888/delete/{id}")
delete.raise_for_status()
print(json.dumps(delete.json(), indent=4, default=str))
