import os
from dataclasses import dataclass
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") or ""


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


@dataclass
class FooBar(db.Model):
    __tablename__ = "foobar"
    id = db.Column(db.Integer, primary_key=True)
    foo = db.Column(db.String)
    bar = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "foo": self.foo, "bar": self.bar}


@app.route(
    "/",
    methods=[
        "GET",
    ],
)
def healthcheck():
    return ""


@app.route(
    "/create",
    methods=[
        "POST",
    ],
)
def create():
    foobar = FooBar(**request.get_json())
    db.session.add(foobar)
    db.session.commit()
    return jsonify(foobar.to_dict())


@app.route(
    "/read/<id>",
    methods=[
        "GET",
    ],
)
def read(id):
    foobar = FooBar.query.filter(FooBar.id == id).first()
    return jsonify(foobar.to_dict())


@app.route(
    "/update/<id>",
    methods=["PUT", "PATCH"],
)
def update(id):
    foobar_update = request.get_json()
    foobar = FooBar.query.filter(FooBar.id == id).first()
    foobar.foo = foobar_update.get("foo") or foobar.foo
    foobar.bar = foobar_update.get("bar") or foobar.bar
    db.session.commit()
    return jsonify(foobar.to_dict())


@app.route(
    "/delete/<id>",
    methods=[
        "DELETE",
    ],
)
def delete(id):
    foobar = FooBar.query.filter(FooBar.id == id).first()
    db.session.delete(foobar)
    db.session.commit()
    return jsonify(foobar.to_dict())
