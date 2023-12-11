import json
import psycopg2

username = 'Marynych_Mukola'
password = 'K30022161K'
database = 'db_lab3'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    tables_name = ['venue', 'year', 'champion']

    data = {}

    for table_name in tables_name:
        cur.execute(f'SELECT * FROM {table_name}')
        rows = cur.fetchall()

        columns = [desc[0] for desc in cur.description]

        table_data = []

        for row in rows:
            row_dict = dict(zip(columns, row))
            table_data.append(row_dict)

        data[table_name] = table_data


with open('exported_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)


