import os
import psycopg2
import re

# Fetch config vars
DATABASE_URL = os.environ['DATABASE_URL']

# Setup db connection
connection =  psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=5432)
cursor = connection.cursor()


def split_on_empty_lines(s):
	# greedily match 2 or more new-lines
	blank_line_regex = r"(?:\r?\n){2,}"
	return re.split(blank_line_regex, s.strip())

albums = ['tcdo', 'lr', 'grad', '808s', 'mbdtf', 'wtt', 'cruel', 'yeezus', 'tlop', 'ye', 'ksg', 'jik']

try:
    for album in albums:
        file_name = 'lyrics/' + album + '.txt' 
        file = open(file_name, "r")
        text = file.read()
        text = split_on_empty_lines(text)
        file.close()
        for lyric in text:
            lyric.replace("\"", "'")
            postgres_insert_query = """ INSERT INTO lyrics(LETRA, ALBUM, LAST_TIME) VALUES (%s,%s,%s)"""
            record_to_insert = (lyric, album, None)
            cursor.execute(postgres_insert_query, record_to_insert)
        
    connection.commit()

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)


finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

print ("Records created successfully");

