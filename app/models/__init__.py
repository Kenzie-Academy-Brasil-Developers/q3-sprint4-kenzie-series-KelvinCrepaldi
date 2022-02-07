from os import getenv
import psycopg2

configs = {
    'host': getenv('DB_HOST'),
    'database': getenv('DB_NAME'),
    'user': getenv('DB_USER'),
    'password': getenv('DB_PASSWORD')
}
class DatabaseConnector:
    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()
        cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS ka_series (
                id              BIGSERIAL       PRIMARY KEY,
                serie           VARCHAR(100)    NOT NULL        UNIQUE,
                seasons         INTEGER         NOT NULL,
                released_date   DATE            NOT NULL,
                genre           VARCHAR(50)     NOT NULL,
                imdb_rating     FLOAT           NOT NULL
            );"""
        )
        
    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()