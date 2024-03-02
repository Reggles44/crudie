from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class PythonFlaskSQLData(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    foo: Mapped[str]
    bar: Mapped[int]


@app.route(
    "/create",
    methods=[
        "POST",
    ],
)
def create():
    new_data = PythonFlaskSQLData(request.get_json())
    db.session.add(**new_data)
    db.session.commit()
    return 200


@app.route(
    "/read",
    methods=[
        "GET",
    ],
)
def read():
    args_dict = request.args.to_dict()
    return db.one_or_404(db.select(PythonFlaskSQLData).filter_by(**args_dict))


@app.route(
    "/update",
    methods=[
        "PATCH",
    ],
)
def update():
    request_dict = request.get_json()
    data = db.one_or_404(db.select(PythonFlaskSQLData).filter_by(**request_dict))
    data.bar = request_dict["bar"]
    db.session.commit()
    return 200


@app.route(
    "/delete",
    methods=[
        "DELETE",
    ],
)
def delete():
    args_dict = request.args.to_dict()
    data = db.one_or_404(db.select(PythonFlaskSQLData).filter_by(**args_dict))
    db.session.delete(data)
    db.session.commit()
    return 200


# Create all db tables
with app.app_context():
    db.create_all()
