from fetch_data_database1 import count_data
from base import connect_database

engine, metadata = connect_database(ulr='postgresql+psycopg2://postgres:user123@localhost/demo')


def sort_by_table_name():
    table_list = []
    for table in metadata.tables.values():
        data = count_data(table)
        table_list.append(data['table'])

    table_list.sort()
    for table in table_list:
        print(table)


if __name__ == "__main__":
    sort_by_table_name()
