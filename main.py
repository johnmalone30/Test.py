import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import file
file='Premier League results data.csv'
df=pd.read_csv('Premier League results data.csv')

#Check file has imported correctly
print(df.head())

# remove some columns that won't be used
df = df.drop(['FTR','HTR','Referee', 'HS', 'AS', 'HST', 'AST', 'HC' ,'AC', 'HF' ,'AF',], axis = 1)

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

#Make columns total yellow cards and total red cards
df['Total Yellow cards']=df['HY']+df['AY']
df['Total Red cards']=df['HR']+df['AR']

# Make a column for comebacks
df['Comeback'] = np.where((df['Final Winner'] != df['Halftime Winner'])&(df['Final Winner']!='Draw')&(df['Halftime Winner']!='Draw'),1, 0)
print(df.columns)

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
precovid_data = pd.DataFrame(precovid_data)
precovid_data.columns=['Total Goals']

#Pre covid Home goals
precovid_data1=precovid_results.groupby('Season')['FTHG'].sum()
precovid_data1 = pd.DataFrame(precovid_data1)
precovid_data1.columns=['Home Goals']

#Pre covid Away goals
precovid_data2=precovid_results.groupby('Season')['FTAG'].sum()
precovid_data2 = pd.DataFrame(precovid_data2)
precovid_data2.columns=['Away Goals']

#Pre covid Comebacks
precovid_data3=precovid_results.groupby('Season')['Comeback'].sum()
precovid_data3 = pd.DataFrame(precovid_data3)
precovid_data3.columns=['Comebacks']

#Number of Games
precovid_data4 = precovid_results.groupby('Season')['Season'].count()
precovid_data4 = pd.DataFrame(precovid_data4)
precovid_data4.columns = ['Games']

#Yellow Cards
precovid_data5 = precovid_results.groupby('Season')['Total Yellow cards'].sum()
precovid_data5 = pd.DataFrame(precovid_data5)
precovid_data5.columns=['Total Yellow Cards']

#Red Cards
precovid_data6 = precovid_results.groupby('Season')['Total Red cards'].sum()
precovid_data6 = pd.DataFrame(precovid_data6)
precovid_data6.columns=['Total Red Cards']


#Mergeing the Dataframes
precovid_data=precovid_data1.merge(precovid_data2, on='Season', how='left')
precovid_data=pd.merge(precovid_data, precovid_data3, on='Season', how ='left')
precovid_data=pd.merge(precovid_data, precovid_data4, on='Season', how ='left')
precovid_data=pd.merge(precovid_data, precovid_data5, on='Season', how ='left')
precovid_data=pd.merge(precovid_data, precovid_data6, on='Season', how ='left')
print(precovid_data)

#Post covid Total scores
postcovid_data=postcovid_results.groupby('Season')['Goals Scored'].sum()
postcovid_data = pd.DataFrame(postcovid_data)
postcovid_data.columns=['Total Goals']

#Post covid Home goals
postcovid_data1=postcovid_results.groupby('Season')['FTHG'].sum()
postcovid_data1 = pd.DataFrame(postcovid_data1)
postcovid_data1.columns=['Home Goals']

#Post covid Away goals
postcovid_data2=postcovid_results.groupby('Season')['FTAG'].sum()
postcovid_data2 = pd.DataFrame(postcovid_data2)
postcovid_data2.columns=['Away Goals']

#Post covid Comebacks
postcovid_data3=postcovid_results.groupby('Season')['Comeback'].sum()
postcovid_data3 = pd.DataFrame(postcovid_data3)
postcovid_data3.columns=['Comebacks']

#Number of Games
postcovid_data4 = postcovid_results.groupby('Season')['Season'].count()
postcovid_data4 = pd.DataFrame(postcovid_data4)
postcovid_data4.columns = ['Games']

#Yellow Cards
postcovid_data5 = postcovid_results.groupby('Season')['Total Yellow cards'].sum()
postcovid_data5 = pd.DataFrame(postcovid_data5)
postcovid_data5.columns=['Total Yellow Cards']

#Red Cards
postcovid_data6 = postcovid_results.groupby('Season')['Total Red cards'].sum()
postcovid_data6 = pd.DataFrame(postcovid_data6)
postcovid_data6.columns=['Total Red Cards']

#Mergeing the Dataframes
postcovid_data=postcovid_data1.merge(postcovid_data2, on='Season', how='left')
postcovid_data=pd.merge(postcovid_data, postcovid_data3, on='Season', how ='left')
postcovid_data=pd.merge(postcovid_data, postcovid_data4, on='Season', how ='left')
postcovid_data=pd.merge(postcovid_data, postcovid_data5, on='Season', how ='left')
postcovid_data=pd.merge(postcovid_data, postcovid_data6, on='Season', how ='left')
print(postcovid_data)

#Joining the dataframes
Covid_Season = pd.concat([precovid_data,postcovid_data])
print(Covid_Season)

#Average nunber of Home and away goals
Covid_Season['Average Home goals']=Covid_Season['Home Goals']/ Covid_Season['Games']
Covid_Season['Average Away goals']=Covid_Season['Away Goals']/ Covid_Season['Games']

#Average Number of Red and Yellow Cards
Covid_Season['Average Yellow goals']=Covid_Season['Total Yellow Cards']/ Covid_Season['Games']
Covid_Season['Average Red goals']=Covid_Season['Total Red Cards']/ Covid_Season['Games']
print( Covid_Season)