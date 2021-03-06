import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Import file
file='Premier League results data.csv'
df=pd.read_csv('Premier League results data.csv')
#Check file has imported correctly
print(df.head())
#Make a column for total goals scored
df['Goals Scored'] = df['FTHG'] + df['FTAG']
# Make columns 'Halftime Winner' and 'Halftime Loser'
conditions = [(df['HTHG'] > df['HTAG']),(df['HTHG'] < df['HTAG'])]
values = [df['HomeTeam'],df['AwayTeam']]
values1 = [df['AwayTeam'],df['HomeTeam']]
df['Halftime Winner'] = np.select(conditions, values, default='Draw')
df['Halftime Loser'] = np.select(conditions, values1, default='Draw')
#Make columns for winner and loser
conditions1 = [(df['FTHG'] > df['FTAG']),(df['FTHG'] < df['FTAG'])]
values2 = [df['HomeTeam'],df['AwayTeam']]
values3 = [df['AwayTeam'],df['HomeTeam']]
df['Final Winner'] = np.select(conditions1, values2, default='Draw')
df['Final Loser'] = np.select(conditions1, values3, default='Draw')
# Make a column for comebacks
df['Comeback'] = np.where((df['Final Winner'] != df['Halftime Winner'])&(df['Final Winner']!='Draw')&(df['Halftime Winner']!='Draw'),1, 0)
print(df.columns)

#Slice the data were need from the file
precovid_results=df.iloc[10044:10332]
postcovid_results=df.iloc[10332:]
precovid_results['Season'].replace({'2019-20':'Pre-Covid'}, inplace=True)
postcovid_results['Season'].replace({'2019-20':'Post-Covid', '2020-21':'Post-Covid'}, inplace=True)
#check head and tail of new dataframes
print(precovid_results.head())
print(precovid_results.tail())
print(postcovid_results.head())
print(postcovid_results.tail())
#Get some overall statistics on the data
print(precovid_results.describe())
print(postcovid_results.describe())
#Pre covid Total scores
precovid_data=precovid_results.groupby('Season')['Goals Scored'].sum()
precovid_data=pd.DataFrame(precovid_data)
precovid_data.columns=['Total Goals']
precovid_data.reset_index(level=0, inplace=True)
#Pre covid Home goals
precovid_data1=precovid_results.groupby('Season')['FTHG'].sum()
precovid_data1=pd.DataFrame(precovid_data1)
precovid_data1.columns=['Home Goals']
precovid_data1.reset_index(level=0,inplace=True)
#Pre covid Away goals
precovid_data2=precovid_results.groupby('Season')['FTAG'].sum()
precovid_data2=pd.DataFrame(precovid_data2)
precovid_data2.columns=['Away Goals']
precovid_data2.reset_index(level=0, inplace=True)
#Pre covid Comebacks
precovid_data3=precovid_results.groupby('Season')['Comeback'].sum()
precovid_data3=pd.DataFrame(precovid_data3)
precovid_data3.columns=['Comebacks']
precovid_data3.reset_index(level=0, inplace=True)
#Mergeing the Dataframes
precovid_data=precovid_data1.merge(precovid_data2, on='Season', how='left')
precovid_data=pd.merge(precovid_data, precovid_data3, on='Season', how ='left')
print(precovid_data)

#Post covid Total scores
postcovid_data=postcovid_results.groupby('Season')['Goals Scored'].sum()
postcovid_data=pd.DataFrame(postcovid_data)
postcovid_data.columns=['Total Goals']
postcovid_data.reset_index(level=0, inplace=True)
#Post covid Home goals
postcovid_data1=postcovid_results.groupby('Season')['FTHG'].sum()
postcovid_data1=pd.DataFrame(postcovid_data1)
postcovid_data1.columns=['Home Goals']
postcovid_data1.reset_index(level=0,inplace=True)
#Post covid Away goals
postcovid_data2=postcovid_results.groupby('Season')['FTAG'].sum()
postcovid_data2=pd.DataFrame(postcovid_data2)
postcovid_data2.columns=['Away Goals']
postcovid_data2.reset_index(level=0, inplace=True)
#Post covid Comebacks
postcovid_data3=postcovid_results.groupby('Season')['Comeback'].sum()
postcovid_data3=pd.DataFrame(postcovid_data3)
postcovid_data3.columns=['Comebacks']
postcovid_data3.reset_index(level=0, inplace=True)
#Mergeing the Dataframes
postcovid_data=postcovid_data1.merge(postcovid_data2, on='Season', how='left')
postcovid_data=pd.merge(postcovid_data, postcovid_data3, on='Season', how ='left')
print(postcovid_data)