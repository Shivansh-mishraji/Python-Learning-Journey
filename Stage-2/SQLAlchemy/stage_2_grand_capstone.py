r""". Custom Exceptions (Stage 1)
Define two domain-specific exceptions:

class EntityNotFoundError(Exception): Raised when a database record is missing. Takes entity_name: str and entity_id: int and formats a clean error message.
class InvalidOrderAmountError(Exception): Raised when an order total is <= 0.

"""
import time
import functools
from sqlalchemy import create_engine, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
import os

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
    
