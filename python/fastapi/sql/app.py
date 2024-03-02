import os
from fastapi import FastAPI, Depends
from sqlmodel import create_engine, SQLModel, Session, Field, select

app = FastAPI()
engine = create_engine(os.getenv("DATABASE_URL") or '', echo=True)


class Crudie(SQLModel):
    id: int = Field(primary_key=True)
    service_key: str


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post("/create", response_model=Crudie)
def create(data: Crudie, session: Session = Depends(get_session)):
    session.add(data)
    session.commit()
    return data


@app.get("/read", response_model=Crudie)
def read(data: Crudie, session: Session = Depends(get_session)):
    result = session.exec(select(Crudie).where(Crudie.service_key == data.service_key)).first()
    return result


@app.patch("/update", response_model=Crudie)
def update(data: Crudie, session: Session = Depends(get_session)):
    result = session.exec(select(Crudie).where(Crudie.service_key == data.service_key)).first()
    result.data = data.data
    session.add(result)
    session.commit()
    return result


@app.delete("/delete", response_model=Crudie)
def delete(data: Crudie, session: Session = Depends(get_session)):
    result = session.exec(select(Crudie).where(Crudie.service_key == data.service_key)).first()
    session.delete(result)
    session.commit()
    return result

