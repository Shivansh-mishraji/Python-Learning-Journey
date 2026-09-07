"""
📋 The 5-Phase Specification:
Phase 1: Setup & Models (Drills 01 & 04)
SQLite database file: kirana_store.db (use os.path and echo=False or True — your choice).
Create Base(DeclarativeBase).
Model 1: Customer (Parent)
id: Integer Primary Key
name: String(50)
phone: String(15)
orders: List of Order objects linked via relationship(back_populates="customer")
Model 2: Order (Child)
id: Integer Primary Key
item_name: String(100)
price: Float
customer_id: Integer Foreign Key pointing to "customers.id"
customer: Single Customer object linked via relationship(back_populates="orders")
Create the tables in the database."""
from sqlalchemy import create_engine, String, Float, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
import os

class Base(DeclarativeBase):
    pass
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/kirana_store.db",echo = False)

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(15))
    orders: Mapped[list["Order"]] = relationship(back_populates = "customer")

class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key = True)
    item_name : Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped[Customer] = relationship(back_populates = "orders")

Base.metadata.create_all(engine)
print("Tables created successfully.")

"""
Phase 2: CREATE via Cascade (Drill 02 & Drill 04)
Open a Session(engine).
Create a customer: "Sharma Ji", phone: "9876543210".
Create 2 orders:
"Atta 5kg", price=250.0
"Mustard Oil 1L", price=180.0
Attach both orders to customer.orders.append(...).
Add only the customer to the session and commit.
Print: "✅ Customer and 2 orders created successfully!"
"""
with Session(engine) as session:
    customer = Customer(name = "Sharma ji", phone = "9876543210" )
    order1 = Order(item_name ="Atta 5kg", price=250.0 )
    order2 = Order(item_name ="Mustard Oil 1L", price=180.0)
    customer.orders.append(order1)
    customer.orders.append(order2)
    session.add(customer)
    session.commit()
    print("✅ Customer and 2 orders created successfully!")

"""Phase 3: READ & Relationship Navigation (Drill 02 & Drill 04)
Open a fresh Session(engine).
Fetch "Sharma Ji" (use session.get(Customer, 1)).
Print: f"Customer: {customer.name} | Phone: {customer.phone}"
Loop through customer.orders and print each item:
Format: f"  -> Item: {order.item_name} | Price: Rs. {order.price}"
Verify the back-link on the first order: print f"  -> Ordered by: {customer.orders[0].customer.name}"
"""
with Session(engine) as session:
    customer = session.get(Customer, 1)
    print(f"Customer: {customer.name} | Phone: {customer.phone}")
    for order in customer.orders :
        print(f"  -> Item: {order.item_name} | Price: Rs. {order.price}")
        if order.id == 1 :
            print(f"  -> Ordered by: {customer.orders[0].customer.name}")

"""Phase 4: UPDATE via Dirty Tracking (Drill 03)
The shopkeeper realizes Mustard Oil price changed from 180 to 195!
Inside a session, find the "Mustard Oil 1L" order.
Change its price directly: order.price = 195.0.
Commit! (Remember: Dirty Tracking automatically updates the database row).
Print: "✅ Price updated to Rs. 195.0 via dirty tracking!"
"""
with Session(engine) as session:
    stmt = select(Order).where(Order.item_name == "Mustard Oil 1L")
    oil_order = session.scalars(stmt).one_or_none()
    if oil_order:
        oil_order.price = 195.0
        session.commit()
        print("✅ Price updated to Rs. 195.0 via dirty tracking!")
"""
Phase 5: DELETE (Drill 03)
Sharma Ji says: "Cancel the Atta, I will take it tomorrow."
Find the "Atta 5kg" order and delete it: session.delete(atta_order).
Commit!
Print: "✅ Atta order deleted!"
Print remaining orders for Sharma Ji to verify only 1 order is left.
"""
with Session(engine) as session:
    stmt = select(Order).where(Order.item_name == "Atta 5kg")
    atta_order = session.scalars(stmt).one_or_none()
    if atta_order:
        session.delete(atta_order)
        session.commit()
        print("✅ Atta order deleted!")
