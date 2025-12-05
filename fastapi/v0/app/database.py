from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# format of a connection string
# <db_provider_name>://<username>:<password>@<ip-address>/<hostname>/<db-name>

SQLALCHEMY_CONNECTION_STRING = "postgres://postgres:password@localhost/SOCIAL_MEDIA"

engine = create_engine(SQLALCHEMY_CONNECTION_STRING)

db_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()