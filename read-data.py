
import pandas as pd
#read a tabular data file into pandas
orders=pd.read_table('http://bit.ly/chiporders')
#orders=pd.read_table('data/chipotle.tsv')
print(orders.head())
user_cols=['used_id','age','gender','occupation','zip_code']
users=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=user_cols)
print(users.head(10))
print(users.tail(10))
print(users.index(10))
