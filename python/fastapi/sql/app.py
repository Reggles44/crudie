import os
from typing import Optional
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
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



@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"defailt": exc.errors(), "body": exc.body},
    )


@app.post("/create", response_model=Crudie)
def create(service_key: str, data: int):
    crudie = Crudie(service_key=service_key, data=data)
    with Session(engine) as session:
        session.add(crudie)
        session.commit()
        session.refresh(crudie)
        return crudie


@app.get("/read", response_model=Crudie)
def read(service_key: str):
    with Session(engine) as session:
        result = session.exec(
            select(Crudie).where(Crudie.service_key == service_key)
        ).first()
        return result


@app.put("/update", response_model=Crudie)
def update(service_key: str, data: int):
    crudie = Crudie(service_key=service_key, data=data)
    with Session(engine) as session:
        result = session.exec(
            select(Crudie).where(Crudie.service_key == crudie.service_key)
        ).first()
        if not result:
            raise
        result.data = crudie.data
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
