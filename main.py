from fastapi import FastAPI
from data_schemas import ProductRequest,ProductResponse
from database import Base,Product
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, scoped_session

app = FastAPI()

MY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    MY_DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300
)


# scoped_session gives each thread/request its own Session automatically
SessionLocal = scoped_session(sessionmaker(bind=engine))

# Create tables automatically
Base.metadata.create_all(engine)
@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str ):
#     return {"item_id": item_id, "q": q}

@app.post("/products")
def create_product(prod : ProductRequest):
    print("name is --------",prod.name)
    print("amount is-------",prod.amount)
    print("date is-------",prod.created_at)
    dbprod= Product(user_id=prod.user_id,name=prod.name,amount=prod.amount,created_at=prod.created_at)
    SessionLocal.add(dbprod)
    SessionLocal.commit()
    return {"test":"prod"}

