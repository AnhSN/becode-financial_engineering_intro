import pandas
from sqlalchemy import create_engine

engine = create_engine('sqlite:///db.sqlite3')
df = pandas.read_csv('database/AAPL.csv')
df.to_sql("AAPL", engine)