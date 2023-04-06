import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aquarius_9789',
        database='gyan_bank'
    )

if __name__ == "__main__":
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM USER")
    for x in cursor:
        print(x)