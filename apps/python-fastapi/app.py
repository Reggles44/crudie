import os

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine

app = FastAPI()
engine = create_engine(os.getenv("DATABASE_URL") or "", echo=True)


class FooBar(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    foo: str
    bar: int


class FooBarUpdate(BaseModel):
    foo: str | None = None
    bar: int | None = None


def get_session() -> Session:
    with Session(engine) as session:
        yield session


@app.get("/")
def healthcheck():
    return


@app.post("/create")
def create(foobar: FooBar, session: Session = Depends(get_session)) -> FooBar:
    session.add(foobar)
    session.commit()
    session.refresh(foobar)
    return foobar


@app.get("/read/{id:int}")
def read(id: int, session: Session = Depends(get_session)) -> FooBar:
    return session.get(FooBar, id)


@app.put("/update/{id:int}")
@app.patch("/update/{id:int}")
def update(
    id: int,
    foobar_update: FooBarUpdate,
    session: Session = Depends(get_session),
) -> FooBar:
    if foobar := session.get(FooBar, id):
        foobar.sqlmodel_update(foobar_update.model_dump(exclude_unset=True))
        session.add(foobar)
        session.commit()
        session.refresh(foobar)
        return foobar
    raise HTTPException(status_code=404, detail="FooBar not found")


@app.delete("/delete/{id:int}")
def delete(id: int, session: Session = Depends(get_session)) -> FooBar:
    if foobar := session.get(FooBar, id):
        session.delete(foobar)
        session.commit()
        return foobar
    raise HTTPException(status_code=437, detail="FooBar not found")
