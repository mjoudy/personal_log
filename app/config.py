import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/dbname")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
