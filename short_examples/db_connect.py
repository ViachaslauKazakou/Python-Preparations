import psycopg2
import traceback
import importlib
def reimport_psycopg2():
    importlib.reload(psycopg2)

try:
    conn = psycopg2.connect(
        user="postgres",
        password="postgres1",
        database="fastapi_service"
    )
    print("Connected to the database")
# except psycopg2.OperationalError as e:
except Exception as e:    
    traceback.print_exc()
    if 'password authentication failed' in str(e):
        print("Invalid username or password")
    else:
        print(f"OperationalError: {e}")
    exit(1)

if conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
    

