import psycopg2
from config.config import Config
from contextlib import contextmanager


class Database_manager:
    def __init__(self, config: Config):
        self.config = config
        self.host = config.DB_HOST
        self.port = config.DB_PORT  
        self.dbname = config.DB_NAME
        self.user = config.DB_USER
        self.password = config.DB_PASSWORD

    @contextmanager
    def get_connection(self):
        conn = None
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            yield conn
        except Exception as e:
            print(f"❌Error connecting to the database: {e}")
            raise
        finally:
            if conn:
                conn.close()

                

        


