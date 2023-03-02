# from fetch_data_database1 import count_data
from base import connect_database

engine, metadata = connect_database(ulr='postgresql+psycopg2://postgres:user123@localhost/demo')


def sort_by_table_name():
    table_list = [table for table in metadata.tables.values()]
    print([x.name for x in table_list])
    # for x in table_list:
    #     print(x.name)


if __name__ == "__main__":
    sort_by_table_name()
