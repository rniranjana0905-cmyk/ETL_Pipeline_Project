from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv() #loads .envfile

def load(df):
  engine=create_engine(os.getenv("DB_URL"))
  df.to_sql("sales", engine,  if_exists="append", index=False)
