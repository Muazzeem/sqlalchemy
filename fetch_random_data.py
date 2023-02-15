# def fetch_table_data(table_name):
#     db_table = Table(table_name, metadata)
#     row_data = []
#     with engine.connect() as con:
#         query = db_table.select().order_by(func.random()).limit(5)
#         result = con.execute(query)
#         for row in result:
#             print(row)
#             row_data.append({"id": row[0], "hash": hash(row)})
#     # json_object = json.dumps(row_data, indent=4)
#     # print(json_object)
#     # with open("db1.json", "w") as outfile:
#     #     outfile.write(json_object)
#
#
# fetch_table_data(table_name='companies_company')

