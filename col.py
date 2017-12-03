import pandas as pd
# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.columns)
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
print(ufo.columns)
ufo_cols=['city','colors reported','shape reported','state','time']
ufo.columns = ufo_cols
print(ufo.columns)
ufo=pd.read_csv('http://bit.ly/uforeports',header=0,names=ufo_cols)
ufo.columns
ufo.columns = ufo.columns.str.replace(' ','_')
ufo.columns
ufo=pd.read_csv('http://bit.ly/uforeports')
ufo.head()
