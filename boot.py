from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import singleton_dabatase_client, singleton
from src.conf import get_postgres_uri
from src.orm import start_mappers

singleton
def bootstrapping():
    start_mappers()
    singleton_db=singleton_dabatase_client('tech_jorge_blanquicett', 'zVbFaMYzyuNz6QJG3tF7oyxL','localhost',5432,'urbvanapi')
    singleton_db.connect()
    return sessionmaker( bind=create_engine(get_postgres_uri(), creator=singleton_db.get_connection, isolation_level="REPEATABLE READ"))