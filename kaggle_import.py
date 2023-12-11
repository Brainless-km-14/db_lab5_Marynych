import csv
import psycopg2

username = 'Marynych_Mukola'
password = 'K30022161K'
database = 'db_lab3'
host = 'localhost'
port = '5432'

csv_file = 'classic-physique-champions.csv'

query_1 = '''
DELETE FROM  year
'''
query_2 = '''
DELETE FROM venue
'''
query_3 = '''
DELETE FROM champion
'''

data_list = []

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cursor = conn.cursor()

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    cursor.execute(query_1)
    cursor.execute(query_2)
    cursor.execute(query_3)
    for row in csv_reader:
        data_list.append(row)


cursor.execute("""
               INSERT INTO venue (city, country,city_id)
               VALUES (%s, %s, %s)
           """, (data_list[4][3].split(',')[0], data_list[4][3].split(',')[1],'2'))

cursor.execute("""
               INSERT INTO venue (city, country,city_id)
               VALUES (%s, %s, %s)
           """, (data_list[2][3].split(',')[0], data_list[2][3].split(',')[1],'1'))



cursor.execute("""
                INSERT INTO champion (name,represented_country,id)
                VALUES (%s,%s,%s)
            """, (data_list[4][5],data_list[4][4],'1'))


cursor.execute("""
                INSERT INTO champion (name,represented_country,id)
                VALUES (%s,%s,%s)
            """, (data_list[2][5],data_list[2][4],'2'))


cursor.execute("""
                INSERT INTO year (year, award$, city_id, id)
                VALUES (%s, %s, %s, %s);
            """, (data_list[4][1], data_list[4][2][1:].replace(",",''),'2' ,'1' ))

cursor.execute("""
                INSERT INTO year (year, award$, city_id, id)
                VALUES (%s, %s, %s, %s);
            """, (data_list[2][1], data_list[2][2][1:].replace(",",''),'1' ,'2' ))

conn.commit()