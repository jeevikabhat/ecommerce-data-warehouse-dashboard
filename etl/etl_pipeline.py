import os
import pandas as pd
from sqlalchemy import create_engine, text
from tqdm import tqdm
from dateutil import parser

# CONFIG
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
OUTPUT_DB = os.path.join(os.path.dirname(__file__), '..', 'output', 'ecommerce_dw.sqlite')

PRODUCTS_CSV = os.path.join(DATA_DIR, 'sample_products.csv')
CUSTOMERS_CSV = os.path.join(DATA_DIR, 'sample_customers.csv')
SALES_CSV = os.path.join(DATA_DIR, 'sample_sales.csv')

# Helper functions
def read_csv(path):
    print(f"Reading {os.path.basename(path)} ...")
    return pd.read_csv(path)

def normalize_products(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    return df

def normalize_customers(df):
    df['email'] = df['email'].str.lower().str.strip()
    return df

def normalize_sales(df):
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['total_amount'] = df['unit_price'] * df['quantity']
    return df

def build_date_dim(dates):
    dates = pd.to_datetime(dates.dropna().unique())
    df = pd.DataFrame({'date': dates})
    df['date_key'] = df['date'].dt.strftime('%Y%m%d').astype(int)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.day_name()
    return df[['date_key','date','year','month','day','day_of_week']]

def main():
    os.makedirs(os.path.dirname(OUTPUT_DB), exist_ok=True)
    engine = create_engine(f"sqlite:///{OUTPUT_DB}", echo=False)

    print("Starting ETL process...")

    products = normalize_products(read_csv(PRODUCTS_CSV))
    customers = normalize_customers(read_csv(CUSTOMERS_CSV))
    sales = normalize_sales(read_csv(SALES_CSV))
    date_dim = build_date_dim(sales['order_date'])

    # Write tables to SQLite
    products.to_sql('dim_product', engine, if_exists='replace', index=False)
    customers.to_sql('dim_customer', engine, if_exists='replace', index=False)
    date_dim.to_sql('dim_date', engine, if_exists='replace', index=False)
    sales.to_sql('fact_sales', engine, if_exists='replace', index=False)

    # Basic counts
    with engine.connect() as conn:
        for table in ['dim_product', 'dim_customer', 'dim_date', 'fact_sales']:
            count = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
            print(f"✅ {table}: {count} rows")

    print(f"ETL completed! Database saved at: {OUTPUT_DB}")

if __name__ == "__main__":
    main()