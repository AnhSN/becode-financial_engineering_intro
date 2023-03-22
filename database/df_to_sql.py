import pandas
from dateutil.parser import parse
from sqlalchemy import Column, Date, Float, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')
df = pandas.read_csv('assets/AAPL.csv', parse_dates=['Date'])
df = df.dropna()

with engine.connect() as connection:
    df.to_sql(
        name='stock_history',
        con=connection,
        if_exists='replace',
        index=True,
        index_label='ID',
        dtype={'Date': Date},
    )
