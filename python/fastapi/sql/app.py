import os
from typing import Optional
from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel, Session, Field, select

app = FastAPI()
engine = create_engine(os.getenv("DATABASE_URL") or "", echo=True)


class Crudie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_key: str
    data: int


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post("/create", response_model=Crudie)
def create(data: Crudie):
    with Session(engine) as session:
        session.add(data)
        session.commit()
        session.refresh(data)
        return data


@app.get("/read", response_model=Crudie)
def read(service_key: str):
    with Session(engine) as session:
        result = session.exec(
            select(Crudie).where(Crudie.service_key == service_key)
        ).first()
        return result


@app.put("/update", response_model=Crudie)
def update(data: Crudie):
    with Session(engine) as session:
        result = session.exec(
            select(Crudie).where(Crudie.service_key == data.service_key)
        ).first()
        result.data = data.data
        session.add(result)
        session.commit()
        session.refresh(result)
        return result


@app.delete("/delete", response_model=Crudie)
def delete(service_key: str):
    with Session(engine) as session:
        result = session.exec(
            select(Crudie).where(Crudie.service_key == service_key)
        ).first()
        session.delete(result)
        session.commit()
        return result
