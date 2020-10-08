import os
import sqlite3
import pandas as pd
import numpy as np


# conn = sqlite3.connect('cities.db', isolation_level=None,
#                            detect_types=sqlite3.PARSE_COLNAMES)

# db_df = pd.read_sql_query("SELECT * FROM vehicles", conn)

# db_df.to_csv('database.csv', index=False)

df = pd.read_csv('vehicles.csv')
df['cylinders'] = df['cylinders'].replace('other', np.nan)
df['cylinders'] = df['cylinders'].str[0]

df.loc[df['cylinders'].notnull(), 'cylinders'] = df.loc[df['cylinders'].notnull(), 'cylinders'].astype(int)

# Filter
df.drop(df.loc[(df.year<2005)].index, axis=0, inplace=True)
df.drop(df.loc[(df.price>15000)|(df.price<3000)].index, axis=0, inplace=True)
df.drop(df.loc[(df.year>2019)].index, axis=0, inplace=True)
df.drop(df.loc[(df.odometer>180000)].index, axis=0, inplace=True)

df.reset_index(drop=True, inplace=True)