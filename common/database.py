from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import environ
from models.models import Model
<<<<<<< HEAD
from sqlalchemy.pool import NullPool

engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URI'),
                       poolclass=NullPool)
=======

engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URI'))
>>>>>>> main
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    Model.query = db_session.query_property()
    Model.metadata.create_all(bind=engine)

