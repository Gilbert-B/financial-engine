import sqlite3
import os

def create_database():
    # 1. Define paths
    # We want the database to live in the root folder, not inside src
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'finance.db')
    sql_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sql', 'ddl', '01_create_tables.sql')

    print(f"Creating database at: {db_path}")

    # 2. Connect to the database (this creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 3. Read the SQL blueprint
    try:
        with open(sql_path, 'r') as sql_file:
            sql_script = sql_file.read()
        
        # 4. Execute the SQL script
        cursor.executescript(sql_script)
        print("✅ Success: Tables created successfully.")
        
        # 5. Verify tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Existing Tables:", [table[0] for table in tables])

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()