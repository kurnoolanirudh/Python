from .database import Base # importing Base from database.py
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text

# models which will be persisted to databse as tables

class Posts(Base):
    __tablename__ = "posts1"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable = False)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    published = Column(Boolean, server_default='FALSE', nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


# once the tables are created in the db if we make some changes to the models.py file they won't get reflected on to the db
# to get the above feature we have to use alembic ??? 

