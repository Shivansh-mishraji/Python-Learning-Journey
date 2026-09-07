"""
Drill 04 Challenge: One-to-Many Relationships & Unit of Work
🎯 Objective:
Build a relational e-commerce order system connecting User (Parent) and Order (Child), seed them via Unit of Work cascading, and verify the two-way relationship in a fresh session.

📋 Technical Specifications:
1. Database & Engine:
SQLite database file: drill_04.db (use os.path so it saves in the exact same directory as your script).
Enable echo=True on create_engine so SQLite prints the underlying SQL statements.
"""
from sqlalchemy import create_engine, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
import os

class Base(DeclarativeBase):
    pass

"""2. Model 1: User (Parent)
Table name: "users"
Columns:
id: Integer Primary Key
name: String(50)
Relationship:
orders: List of Order objects linked via relationship() with back_populates="user".
"""
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    orders: Mapped[list["Order"]] = relationship(back_populates = "user")
"""3. Model 2: Order (Child)
Table name: "orders"
Columns:
id: Integer Primary Key
item_name: String(100)
price: Float
user_id: Integer Foreign Key pointing to "users.id"
Relationship:
user: Single User object linked via relationship() with back_populates="orders".
"""
class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key = True)
    item_name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    user: Mapped[User] = relationship(back_populates = "orders")
"""4. Table DDL:
Generate the tables in the database (Base.metadata.create_all(engine)).
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/drill_04.db", echo = False)
print("Database created successfully")

Base.metadata.create_all(engine)
print("Tables Created Successfully")
"""
5. Session 1 — Relational Insert via Unit of Work:
Open with Session(engine) as session:
Instantiate User(name="Shivansh").
Instantiate two Order objects:
"Mechanical Keyboard", price=4500.0
"Wireless Mouse", price=1200.0
Attach both orders to user.orders using .append().
Call session.add(user) (do NOT manually add the orders — let SQLAlchemy cascade them).
Commit the session.
"""
with Session(engine) as session:
    user = User(name = "Shivansh")
    order1 = Order(item_name = "Mechanical Keyboard", price=4500.0)
    order2 = Order(item_name = "Wireless Mouse", price=1200.0)
    user.orders.append(order1)
    user.orders.append(order2)
    session.add(user)
    session.commit()
"""
6. Session 2 — Relational Query & Verification:
Open a fresh with Session(engine) as session:
Fetch the user with ID 1 (use session.get(User, 1)).
Print the user's name: f"User: {user.name}".
Loop through user.orders and print each item:
Format: f"  -> Order #{order.id}: {order.item_name} | Price: ₹{order.price}"
Pick the first order and print: f"  -> Verified Back-link: {user.orders[0].user.name}".
"""
with Session(engine) as session:
    user = session.get(User, 1)
   
    print(f"User: {user.name}")
    for order in user.orders:
        print(f"  -> Order #{order.id}: {order.item_name} | Price: Rs. {order.price}")
        if order.id == 1 :
            print(f"  -> Verified Back-link: {user.orders[0].user.name}")
    