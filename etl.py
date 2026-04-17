import pandas as pd
from db import load
def extract(path):
  df=pd.read_csv(path)
  print("Extracted data:")
  print(df)
  return df
def transform(df):
  #drop rows with missing order id
  df=df.dropna(subset=["Order ID"])

  #fill missing amount with 0
  df["Sales"]= df["Sales"].fillna(0)

  #drop invalid date
  df=df.dropna(subset=["Order Date"])

print("\nTransformed data:")
print(df)
return df

def run_etl():
  df=extract("data/superstore_sales_dataset.csv")
  df=transform(df)
  load(df)
if __name__=="__main__":
  run_etl()
