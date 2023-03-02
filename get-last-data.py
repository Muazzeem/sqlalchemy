from sqlalchemy import MetaData, create_engine, URL
import hashlib
from sqlalchemy import desc
from sqlalchemy.inspection import inspect

db_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="user123",
    host="localhost",
    database="demo"
)

engine = create_engine(db_url)
metadata = MetaData()
metadata.reflect(engine)

table_list = [table for table in metadata.tables.values()]
tables = [x.name for x in table_list]


def convert_to_str(row):
    return tuple([str(col_val) for col_val in row])


def create_hash(row):
    m = hashlib.md5()
    for s in row:
        m.update(s.encode())
    return m.hexdigest()


def get_last_rows(table_name):
    table = metadata.tables[table_name]
    try:
        primary_key = inspect(table).primary_key.columns.keys()[0]
        val = getattr(table.c, primary_key)
        print(val)
        query = table.select().order_by(desc(val)).limit(5)
        with engine.connect() as conn:
            row_list = reversed(conn.execute(query).fetchall())

    except Exception as ex:
        print(ex)
        print(table_name)

    else:
        for data in row_list:
            print(create_hash(convert_to_str(data)), table_name)


for x in tables:
    get_last_rows(table_name=x)
