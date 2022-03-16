import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
import logging
from models.models import Base




DB_ECHO = False
DB_AUTOCOMMIT = True

def create_session_from_url(uri):
  engine = create_engine(uri)
  maker = sessionmaker(bind = engine)
  return engine, maker

def db_session():
  from config import make_settings
  _, DEFAULT_SESSION_MAKER = create_session_from_url(make_settings().db_uri)
  return scoped_session(DEFAULT_SESSION_MAKER)

def create_all(engine: Engine = None):
  from config import make_settings
  if engine is None:
    engine, _ = create_session_from_url(make_settings().db_uri)
#  Base.metadata.create_all(engine)
  return engine

def get_engine(uri):
    logging.info('Connecting to database..')
    options = {
        'echo': DB_ECHO,
        'execution_options': {
            'autocommit': DB_AUTOCOMMIT
        }
    }
    return create_engine(uri, **options)



