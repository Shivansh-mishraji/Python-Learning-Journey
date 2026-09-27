"""  Phase 1 Specification: Systems Foundation & Relational Schema

 Custom Exceptions (Stage 1)
Define two domain-specific exceptions:

class EntityNotFoundError(Exception): Raised when a database record is missing. Takes entity_name: str and entity_id: int and formats a clean error message.
class InvalidOrderAmountError(Exception): Raised when an order total is <= 0.

"""
import time
import functools
from sqlalchemy import create_engine, String, Float, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
import os
from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI, Depends

app = FastAPI()

class EntityNotFoundError(Exception):
    def __init__(self, entity_name: str, entity_id: int):
        self.entity_name = entity_name
        self.entity_id = entity_id
        super().__init__(f"{entity_name} with id {entity_id} not found.")

class InvalidOrderAmountError(Exception):
    def __init__(self, order_total: float):
        self.order_total = order_total
        super().__init__(f"Order amount {order_total} is invalid. Amount must be greater than 0.")

"""2. The @timer Decorator (Stage 1)
Use functools.wraps(func).
Measure execution time with time.perf_counter().
Print [LATENCY] {func.__name__} completed in {duration_ms:.2f}ms.
Return the uncalled wrapper."""
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration_ms = (time.perf_counter() - start) * 1000
        print(f"[LATENCY] {func.__name__} completed in {duration_ms:.2f}ms.")
        return result
    return wrapper

"""
3. Database Engine & Relational Schema (Stage 2A & 2B)
Database path: SQLite file store_capstone.db in the same directory using os.path.dirname(os.path.abspath(__file__)).
Create Base(DeclarativeBase).
Model 1: Customer
id: Mapped[int], primary key.
name: Mapped[str], String(50).
email: Mapped[str], String(100), unique.
orders: Mapped[list["Order"]], relationship with back_populates="customer", cascade "all, delete-orphan".
Model 2: Order
id: Mapped[int], primary key.
total: Mapped[float], Float.
customer_id: Mapped[int], ForeignKey("customers.id").
customer: Mapped["Customer"], relationship with back_populates="orders".
Call Base.metadata.create_all(engine)."""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "store_capstone.db")
engine = create_engine(f"sqlite:///{db_path}", echo=False)

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="customer", cascade="all, delete-orphan")

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    total: Mapped[float] = mapped_column(Float)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped["Customer"] = relationship(back_populates="orders")

Base.metadata.create_all(engine)
print("Tables had been created")

"""   Phase 2: Pydantic v2 Schemas & Database Dependency Injection

Now we build the bridge between HTTP requests, validation, and database sessions.

Write the following into 

stage_2_grand_capstone.py
:

Pydantic v2 Schemas (pydantic.BaseModel):

OrderCreate: total: float
OrderResponse: id: int, total: float, customer_id: int with model_config = ConfigDict(from_attributes=True)
CustomerCreate: name: str, email: str
CustomerResponse: id: int, name: str, email: str, orders: list[OrderResponse] = [] with model_config = ConfigDict(from_attributes=True)
Session Dependency Injection (get_db):

A generator function get_db() that yields a Session(engine) 
"""
class OrderCreate(BaseModel):
    total: float

class OrderResponse(BaseModel):
    id: int
    total: float
    customer_id: int

    model_config = ConfigDict(from_attributes=True)

class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    orders: list[OrderResponse] = []

    model_config = ConfigDict(from_attributes=True)

def get_db():
    with Session(engine) as session:
        yield session

#----------------------------------------------------------------------------------------------------------

@app.get("/")
def home():
    return "Welcome to My Capstone Project"

@app.get("/health")
def health():
    return {
            "status_code": 200,
            "responce": "Backend is working Properly"
            }

"""  🚀 Phase 3 Specification: Service Layer (CRUD Logic & Exceptions with @timer)

implement the following 4 service functions (remember to import select from sqlalchemy if needed):

1. create_customer(session: Session, data: CustomerCreate) -> Customer
Decorated with @timer.
Instantiate Customer(name=data.name, email=data.email).
Add to session, session.commit(), session.refresh(customer), and return the customer.
2. get_customer(session: Session, customer_id: int) -> Customer
Decorated with @timer.
Query customer using session.get(Customer, customer_id) (or session.scalars(select(Customer).where(Customer.id == customer_id)).first()).
Exception Guard: If customer is None, raise:
python
raise EntityNotFoundError(entity_name="Customer", entity_id=customer_id)
Return the found customer."""


# =============================================================
# SERVICE LAYER — Pure business logic, no FastAPI here
# These functions can be tested independently without HTTP
# =============================================================

@timer
def create_customer(db: Session, data: CustomerCreate) -> Customer:
    new_customer = Customer(name=data.name, email=data.email)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@timer
def get_customer(db: Session, customer_id: int) -> Customer:
    result = db.get(Customer, customer_id)
    if result is None:
        raise EntityNotFoundError(entity_name="Customer", entity_id=customer_id)
    return result

@timer
def create_order(db: Session, customer_id: int, data: OrderCreate) -> Order:
    if data.total <= 0:
        raise InvalidOrderAmountError(order_total=data.total)
    get_customer(db, customer_id)  # raises EntityNotFoundError if missing
    new_order = Order(total=data.total, customer_id=customer_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@timer
def get_customer_orders(db: Session, customer_id: int) -> list[Order]:
    customer = get_customer(db, customer_id)  # raises EntityNotFoundError if missing
    return customer.orders


# =============================================================
# API ENDPOINTS — Just the door. Calls services, returns responses.
# =============================================================

@app.post("/customers", status_code=201, response_model=CustomerResponse)
def create_customer_endpoint(data: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, data)

@app.get("/customers/{customer_id}", status_code=200, response_model=CustomerResponse)
def get_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(db, customer_id)

@app.post("/orders", status_code=201, response_model=OrderResponse)
def create_order_endpoint(customer_id: int, data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, customer_id, data)

@app.get("/orders/{customer_id}", status_code=200, response_model=list[OrderResponse])
def get_customer_orders_endpoint(customer_id: int, db: Session = Depends(get_db)):
    return get_customer_orders(db, customer_id)
