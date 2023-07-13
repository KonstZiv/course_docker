from psycopg2 import OperationalError, connect
import os


name = os.environ["POSTGRES_DB"]
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["DB_HOST"]
port = os.environ["DB_PORT"]


def create_connection(
    db_name=name,
    db_user=user,
    db_password=password,
    db_host=host,
    db_port=port,
):
    try:
        print("try connection...")
        connection = connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful.")
    except OperationalError as err:
        print(f"The error '{err}' occured.")
        connection = None
    return connection


conn = create_connection()
