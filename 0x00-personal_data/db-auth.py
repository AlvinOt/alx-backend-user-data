import os
import psycopg2

# Fetch database credentials from environment variables
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

# Establish a database connection
try:
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )

    # Perform database operations here

    print("Database connection established successfully!")

except psycopg2.Error as e:
    print(f"Unable to connect to the database. Error: {e}")

finally:
    # Close the connection when done
    if connection:
        connection.close()
        print("Database connection closed.")
