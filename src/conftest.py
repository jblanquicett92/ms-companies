import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from orm import metadata, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine('postgresql+psycopg2://tech_jorge_blanquicett:zVbFaMYzyuNz6QJG3tF7oyxL@localhost:5437/urbvanapi') 
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()
