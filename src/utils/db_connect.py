import sqlalchemy
import urllib

def get_db_connection():
    """
    Establishes a connection to the Local MSSQL Server.
    Returns: SQLAlchemy Engine
    """
    # ---------------------------------------------------------
    # CONFIGURATION (Edit this section)
    # ---------------------------------------------------------
    SERVER_NAME = 'GILB-PREDATOR'  # <--- PASTE YOUR SERVER NAME HERE
    DATABASE_NAME = 'Financial_DB'
    DRIVER = 'ODBC Driver 17 for SQL Server'
    # Note: If 'ODBC Driver 17' fails, try 'SQL Server'
    # ---------------------------------------------------------

    # Create the connection string (Trusted_Connection=yes means use Windows Auth)
    params = urllib.parse.quote_plus(
        f'DRIVER={{{DRIVER}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;'
    )
    
    connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

    try:
        engine = sqlalchemy.create_engine(connection_string)
        # Test the connection
        with engine.connect() as conn:
            print(f"✅ Successfully connected to: {SERVER_NAME} -> {DATABASE_NAME}")
        return engine
    except Exception as e:
        print(f"❌ Connection Failed. Error: {e}")
        return None

if __name__ == "__main__":
    get_db_connection()