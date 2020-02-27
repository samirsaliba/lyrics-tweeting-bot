import os
import psycopg2
from datetime import datetime
import random as rd


# Fetch config vars
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
DATABASE_URL = os.environ['DATABASE_URL']

# Setup db connection
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connection.cursor()

# Twitter auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


try:
    postgreSQL_select_Query = "select * \
        from lyrics \
        ORDER BY last_time NULLS FIRST \
        fetch first 100 rows only"

    cursor.execute(postgreSQL_select_Query)

    query = cursor.fetchall()
    aux = rd.randint(0, 100)
    index, lyric, album, date = query[aux]
    date = datetime.now()

    sql_update_query = """Update lyrics set last_time = %s where id = %s"""
    cursor.execute(sql_update_query, (date, index))
    
	api.update_status(lyric)
    connection.commit()

    print ("Tweet sent!");

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Error: ", error)
    

finally:
    # Closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



