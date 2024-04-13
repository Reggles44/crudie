import os
import traceback
from typing import Optional
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlmodel import create_engine, SQLModel, Session, Field, select

app = FastAPI()
engine = create_engine(os.getenv("DATABASE_URL") or "", echo=True)


class Crudie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_key: str
    data: int


class InvalidServiceKey(Exception):
    pass


@app.exception_handler(RequestValidationError)
def validation_request_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    traceback.print_exc()
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.exception_handler(InvalidServiceKey)
def invalid_service_key_handler(
    request: Request, exc: InvalidServiceKey
) -> JSONResponse:
    traceback.print_exc()
    loc_type = "query" if request.method in ("GET", "DELETE") else "body"
    return JSONResponse(
        status_code=status.HTTP_428_PRECONDITION_REQUIRED,
        content=jsonable_encoder(
            {
                "details": [
                    {
                        "type": "invalid",
                        "loc": [loc_type, "service_key"],
                        "msg": "service_key was not valid",
                    }
                ],
                "body": str(request.body()),
            }
        ),
    )


@app.post("/create", response_model=Crudie)
def create(crudie: Crudie):
    if not crudie.service_key:
        raise RequestValidationError(
            errors=[
                {
                    "type": "invalid",
                    "loc": ["body", "service_key"],
                    "msg": "missing service_key",
                }
            ]
        )
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
def update(crudie: Crudie):
    if not crudie.service_key:
        raise RequestValidationError(
            errors=[
                {
                    "type": "invalid",
                    "loc": ["body", "service_key"],
                    "msg": "missing service_key",
                }
            ]
        )
    with Session(engine) as session:
        result = session.exec(
            select(Crudie).where(Crudie.service_key == crudie.service_key)
        ).first()
        if not result:
            raise InvalidServiceKey("service_key not in database")
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
        if not result:
            raise InvalidServiceKey("service_key not in database")
        session.delete(result)
        session.commit()
        return result
