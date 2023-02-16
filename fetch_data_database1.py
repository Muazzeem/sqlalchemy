from sqlalchemy import Table
from base import connect_database

engine, metadata = connect_database(ulr='postgresql+psycopg2://postgres:user123@localhost/demo')


def count_data(table):
    table = Table(table.name, metadata, autoload=True, autoload_with=engine)
    select_query = table.select()

    with engine.connect() as conn:
        row_count = conn.execute(select_query).rowcount
        return {'table': table.name, 'item': row_count}


data_list = [count_data(table) for table in metadata.tables.values()]
sorted_data = sorted(data_list, key=lambda x: x['table'])
for data in sorted_data:
    print(f"{data['table']}: {data['item']}")

