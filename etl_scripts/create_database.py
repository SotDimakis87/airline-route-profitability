from sqlalchemy import create_engine, text

DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

# connect to default database "postgres"
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"
)

with engine.connect() as conn:
    conn = conn.execution_options(isolation_level="AUTOCOMMIT")
    
    conn.execute(text("CREATE DATABASE airline_db"))

print("Database 'airline_db' created successfully")