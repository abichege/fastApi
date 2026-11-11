from math import prod

from fastapi import FastAPI
from data_schemas import ProductRequest,ProductResponse,SaleRequest,SaleResponse,PaymentRequest,PaymentResponse,StockRequest,StockResponse
from database import Base,Product,User,Sale,Payment,Stock
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime, timedelta

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

# add user running only once
# def add_user():
#     user=User(full_name="Abi",email="abi@mail.com",password="12345",created_at=datetime.utcnow())
#     SessionLocal.add(user)
#     SessionLocal.commit()

# add_user()  # Call the function to add the user

@app.post("/products",response_model=ProductResponse)
def create_product(prod : ProductRequest):
    print("name is --------",prod.name)
    print("amount is-------",prod.amount)
    print("date is-------",prod.created_at)
    dbprod= Product(user_id=prod.user_id,name=prod.name,amount=prod.amount,created_at=prod.created_at)
    SessionLocal.add(dbprod)
    SessionLocal.commit()
    return dbprod

@app.get("/products",response_model=list[ProductResponse])
def get_products():
    query = select(Product)
    all_products = list(SessionLocal.scalars(query).all())

    return all_products

@app.post("/sales",response_model=SaleResponse)
def create_sale(sale: SaleRequest):
    db_sale = Sale(product_id=sale.product_id, created_at=sale.created_at)
    print("product_id is --------", sale.product_id)
    print("date is-------", sale.created_at)
    SessionLocal.add(db_sale)
    SessionLocal.commit()
    return db_sale

@app.get("/sales",response_model=list[SaleResponse])
def get_sales():
    query = select(Sale)
    all_sales = list(SessionLocal.scalars(query).all())

    return all_sales

@app.post("/payments",response_model=PaymentResponse)
def create_payment(payment: PaymentRequest):
    db_payment = Payment(
        sale_id=payment.sale_id,
        mrid=payment.mrid,
        crid=payment.crid,
        trans_code=payment.trans_code,
        trans_amount=payment.trans_amount,
        phone_paid=payment.phone_paid,
        status=payment.status,
        created_at=payment.created_at
    )
    print("sale_id is --------", payment.sale_id)
    print("mrid is --------", payment.mrid)
    print("crid is --------", payment.crid)
    print("trans_code is --------", payment.trans_code)
    print("trans_amount is --------", payment.trans_amount)
    print("phone_paid is --------", payment.phone_paid)
    print("status is --------", payment.status)
    print("date is-------", payment.created_at)

    SessionLocal.add(db_payment)
    SessionLocal.commit()
    return db_payment

@app.get("/payments",response_model=list[PaymentResponse])
def get_payments():
    query = select(Payment)
    all_payments = list(SessionLocal.scalars(query).all())

    return all_payments

@app.post("/stock",response_model=StockResponse)
def create_stock(stock: StockRequest):
    db_stock = Stock(
        product_id=stock.product_id,
        quantity=stock.quantity,
        updated_at=stock.updated_at
    )
    print("product_id is --------", stock.product_id)
    print("quantity is --------", stock.quantity)
    print("date is-------", stock.updated_at)

    SessionLocal.add(db_stock)
    SessionLocal.commit()
    return db_stock

@app.get("/stock",response_model=list[StockResponse])
def get_stock():        
    query = select(Stock)
    all_stock = list(SessionLocal.scalars(query).all())

    return all_stock
