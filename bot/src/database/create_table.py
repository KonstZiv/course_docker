from .connection import conn
from psycopg2 import OperationalError


def execute_query(query, connection=conn):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully.")
    except OperationalError as err:
        print(f"The error '{err}' ocured.")


create_message_table = """
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    message TEXT,
    user_id BIGINT NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
)
"""

execute_query(create_message_table)
