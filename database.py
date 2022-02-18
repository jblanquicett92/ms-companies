import sys, psycopg2, psycopg2.sql

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
          instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class singleton_dabatase_client:

    def __init__(self, user, password, host, port, dbname):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.connection=None

    def connect(self):
        self.connection = psycopg2.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            dbname = self.dbname
            )

        print(" * Connected to database: %s" % self.dbname)


    def get_connection(self):
        return self.connection