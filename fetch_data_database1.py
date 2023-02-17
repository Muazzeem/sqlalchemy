from sqlalchemy import Table, MetaData, create_engine, URL, text

db_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="user123",
    host="localhost",
    database="demo",
)

engine = create_engine(db_url)
metadata = MetaData()
metadata.reflect(engine)


def count_data(table):
    table = Table(table.name, metadata, autoload=True, autoload_with=engine)
    with engine.connect() as conn:
        query = f"select count(id) from {table.name}"
        count = conn.execute(text(query)).scalar()
        return {'table': table.name, 'item': count}


data_list = [count_data(table) for table in metadata.tables.values() if 'id' in table.columns]
table_list = sorted(data_list, key=lambda x: x['table'])
for data in table_list:
    print(f"{data['table']}: {data['item']}")
