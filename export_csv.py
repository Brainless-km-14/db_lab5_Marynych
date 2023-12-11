import csv
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

    for table_name in tables_name:
        cur.execute(f'SELECT * FROM {table_name}')
        rows = cur.fetchall()

        columns = [desc[0] for desc in cur.description]

        with open(f'{table_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            csv_writer.writerow(columns)

            csv_writer.writerows(rows)

