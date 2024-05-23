import os
import psycopg2

def main():
    conn = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT")
    )
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    print(f"Connected to PostgreSQL database! Version: {db_version[0]}")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
