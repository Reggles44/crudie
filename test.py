import os
import sys
import git
import pytest
import argparse
import requests

MODULE = sys.modules[__name__]
path = os.path.dirname(os.path.realpath(__file__))
repo = git.Repo(path)
submodule_paths = [os.path.split(sm.abspath) for sm in repo.submodules]

arg_parser = argparse.ArgumentParser(
    prog="CRUD.ie",
    description="The testing script for CRUD.ie",
)
arg_parser.add_argument("paths", nargs="*", choices=submodule_paths)

CREATE_DATA = {"foo": "abc", "bar": 123}
READ_DATA = {"foo": "abc"}
UPDATE_DATA = {"foo": "abc", "bar": 789}
DELETE_DATA = {"foo": "abc"}


def create(path):
    response = requests.post(path, json=CREATE_DATA)
    response.raise_for_status()
    assert response.json() == CREATE_DATA


def read(path):
    response = requests.get(path, data=READ_DATA)
    response.raise_for_status()
    assert response.json() == CREATE_DATA


def update(path):
    response = requests.patch(path, json=UPDATE_DATA)
    response.raise_for_status()
    assert response.json() == UPDATE_DATA


def delete(path):
    response = requests.delete(path, data=DELETE_DATA)
    response.raise_for_status()
    assert response.json() == UPDATE_DATA


args = arg_parser.parse_args()
for path in args.paths or submodule_paths:

    @pytest.mark.parametrize("func", [create, read, update, delete])
    def run(func):
        func(path)

    setattr(MODULE, f'test_{"_".join(path)}', run)


def test_if_tests_exist():
    base_tests = ["test_if_tests_exist", "test_duplicate_name"]
    dynamic_tests = [
        var for var in dir(MODULE) if var.startswith("test_") and var not in base_tests
    ]
    assert len(dynamic_tests) > 0, dynamic_tests
