import os
import json
from dataclasses import dataclass, asdict
from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") or ""

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


@dataclass
class Crudie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_key = db.Column(db.String)
    data = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "service_key": self.service_key, "data": self.data}


@app.route("/create", methods=["POST", ])
def create():
    data = Crudie(**request.get_json())
    db.session.add(data)
    db.session.commit()
    return jsonify(data.to_dict())

@app.route("/read", methods=["GET", ])
def read():
    service_key = request.args.to_dict().get("service_key")
    data = Crudie.query.filter(Crudie.service_key == service_key).first()
    return jsonify(data.to_dict())


@app.route("/update", methods=["PUT", ])
def update():
    service_key = request.get_json().get("service_key")
    data = Crudie.query.filter(Crudie.service_key == service_key).first()
    data.data = request.get_json()["data"]
    db.session.commit()
    return jsonify(data.to_dict())


@app.route("/delete", methods=["DELETE", ])
def delete():
    service_key = request.args.to_dict().get("service_key")
    data = Crudie.query.filter(Crudie.service_key == service_key).first()
    db.session.delete(data)
    db.session.commit()
    return jsonify(data.to_dict())


with app.app_context():
    db.create_all()
