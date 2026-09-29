# models.py — sqlalchemy models
# import Base from database.py  ← new thing in multi-file
from database import Base, engine
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
# create two models:
#
# User → id, name, email(unique), applications(relationship)
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]= mapped_column(String(40), unique= True)
    applications: Mapped[list["Application"]] = relationship(back_populates = "user")
# Application → id, company, role, status, job_description, user_id(FK), user(relationship)
class Application(Base):
    __tablename__ = "application"

    id: Mapped[int] = mapped_column(primary_key = True)
    company: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(20))
    job_description: Mapped[str] = mapped_column(String(10000))
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    user: Mapped[User] = relationship(back_populates = "applications")

# at the bottom: Base.metadata.create_all(engine)
Base.metadata.create_all(engine)
# import engine from database.py for that
