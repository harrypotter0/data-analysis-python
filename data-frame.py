
import pandas as pd

#select a pandas Series from a DataFrame
ufo=pd.read_table('http://bit.ly/uforeports',sep=',')
ufo=pd.read_csv('http://bit.ly/uforeports')#separator is already assumed
print(ufo.head())
print(ufo['City'])
ufo['Location'] = ufo.City + ', ' + ufo.State
print(ufo.head())
movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())
print(movies.describe())
print(movies.shape)# example attribute: number of rows and columns
print(movies.dtypes)# example attribute: data type of each column
print(movies.describe(include=['object']))
