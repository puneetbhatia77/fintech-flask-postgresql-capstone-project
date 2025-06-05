import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
print("🔄 Loading environment variables from .env")
def init_db():
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("❌ DB_URL not found in .env")

    print(f"DB URL: {db_url}")

    engine = create_engine(db_url)
    with engine.begin() as conn:
        conn.execute(text("""
               CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(150) UNIQUE NOT NULL,
                    password_hash VARCHAR(512) NOT NULL
             )
        """))
    print("✅ Database tables created")
