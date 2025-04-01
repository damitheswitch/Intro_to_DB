import mysql.connector
from mysql.connector import errorcode

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='',
            password=''
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied - invalid username or password")
        else:
            print(f"Error connecting to MySQL: {err}")
        return None  # Return None if connection fails

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

def main():
    connection = connect_to_mysql()
    
    if connection is not None:  # Corrected check
        try:
            cursor = connection.cursor()
            create_database(cursor)
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    main()

