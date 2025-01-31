import mysql.connector

def create_alx_book_store_database(host, user, password):

    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        cursor = connection.cursor()

        create_database_query = "CREATE DATABASE alx_book_store"
        cursor.execute(create_database_query)
        connection.commit()

        print("Database 'alx_book_store' created successfully.")

    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

    finally:
        if connection:
            connection.cursor().close()
            connection.close()

host = "your_mysql_host"
user = "your_mysql_username"
password = "your_mysql_password"

create_alx_book_store_database(host, user, password)