import pymysql
import pymysql.cursors
from contextlib import contextmanager
from config import DATABASE_SETTINGS

@contextmanager
def conexao(
        host=DATABASE_SETTINGS['HOST'],
        user=DATABASE_SETTINGS['USER'],
        password=DATABASE_SETTINGS['PASSWORD'],
        database=DATABASE_SETTINGS['DATABASE'],
        charset=DATABASE_SETTINGS['CHARSET'],
        cursorclass=pymysql.cursors.DictCursor
):
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        charset=charset,
        cursorclass=cursorclass
    )
    try:

        yield conn
    finally:
        conn.close()
