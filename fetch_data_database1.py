from sqlalchemy import Table
from base import connect_database

engine, metadata = connect_database(ulr='postgresql+psycopg2://postgres:user123@localhost/demo')


def count_data(table):
    table = Table(table.name, metadata, autoload=True, autoload_with=engine)
    select_query = table.select()

    with engine.connect() as conn:
        row_count = conn.execute(select_query).rowcount
        data = {'table': table.name, 'item': row_count}
        return data


def sort_by_key(table_list):
    return table_list['table']


def sort_data_output():
    data_list = []
    for table in metadata.tables.values():
        x = count_data(table)
        data_list.append(x)
    sorted_data = sorted(data_list, key=sort_by_key)
    for data in sorted_data:
        print(data['table'], data['item'], sep=": ")


if __name__ == "__main__":
    sort_data_output()
