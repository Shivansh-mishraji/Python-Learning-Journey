"""Requirements:
1:Database & Engine:

SQLite database: store.db (in the same directory using os.path).
Create Base(DeclarativeBase).
Model Product:
id: Integer Primary Key
name: String(50)
price: Float
Create tables: Base.metadata.create_all(engine).
"""
from sqlalchemy import create_engine, String, Float,select
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column, Session
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/store.db", echo = False)
class Base(DeclarativeBase):
    pass
class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)

Base.metadata.create_all(engine)
print("Tables created successfully")

"""
2: Dependency get_db():

A generator yielding a Session(engine) using with Session(engine) as session: yield session.

3: Pydantic Schemas:

ProductCreate: name: str, price: float (Input)
ProductResponse: id: int, name: str, price: float with model_config = ConfigDict(from_attributes=True) (Output)
"""
def get_db():
    with Session(engine) as session:
        yield session

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponce(BaseModel):
    id: int
    name: str
    price: float
    model_config = ConfigDict(from_attributes = True)

"""
4: FastAPI App & Endpoints:

POST /products (status code 201, response_model=ProductResponse):
Takes payload: ProductCreate and db: Session = Depends(get_db).
Creates, commits, refreshes, and returns the new Product.
GET /products (response_model=list[ProductResponse]):
Queries all products using select(Product) and returns them.
GET /products/{id} (response_model=ProductResponse):
Fetches by ID using db.get(Product, id).
If not found, raises HTTPException(status_code=404, detail="Product not found").
Returns the product.
"""

app = FastAPI()

@app.post("/products", status_code = 201, response_model = ProductResponce)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name = payload.name, price = payload.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products", response_model = list[ProductResponce])
def get_products(db: Session = Depends(get_db)):
    products = db.scalars(select(Product)).all()
    if not products:
        raise HTTPException(status_code = 404, details = "Product not found")
    return products


@app.get("/products/{id}", response_model = ProductResponce)
def get_a_product(id: int, db: Session = Depends(get_db)):
    products = db.get(Product, id)
    if not products:
        raise HTTPException(status_code = 404, details = "Product not found")
    return products





