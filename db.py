from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv() #loads .envfile

def load(df):
   try:
        logging.info("Loading data to database...")
        engine=create_engine(os.getenv("DB_URL"))
        df.to_sql("sales", engine,  if_exists="append", index=False)

        logging.info("Data loaded successfully!")

    except Exception as e:
        logging.error(f"Error: {e}")
