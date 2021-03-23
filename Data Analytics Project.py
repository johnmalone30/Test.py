import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import file
file = 'Premier League results data.csv'
df = pd.read_csv('Premier League results data.csv')

# Check file has imported correctly
print(df.head())

# remove some columns that won't be used
df = df.drop(['FTR', 'HTR', 'Referee', 'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'HF', 'AF', ], axis=1)

# Make columns 'Halftime Winner' and 'Halftime Loser'
conditions = [(df['HTHG'] > df['HTAG']), (df['HTHG'] < df['HTAG'])]
values = [df['HomeTeam'], df['AwayTeam']]
values1 = [df['AwayTeam'], df['HomeTeam']]
df['Halftime Winner'] = np.select(conditions, values, default='Draw')
df['Halftime Loser'] = np.select(conditions, values1, default='Draw')

# Make columns for winner and loser
conditions1 = [(df['FTHG'] > df['FTAG']), (df['FTHG'] < df['FTAG'])]
values2 = [df['HomeTeam'], df['AwayTeam']]
values3 = [df['AwayTeam'], df['HomeTeam']]
df['Final Winner'] = np.select(conditions1, values2, default='Draw')

# Make columns total yellow cards and total red cards
df['Total Yellow cards'] = df['HY'] + df['AY']
df['Total Red cards'] = df['HR'] + df['AR']

# Make a column for comebacks
df['Comeback'] = np.where((df['Final Winner'] != df['Halftime Winner']) & (df['Final Winner'] != 'Draw') & (df['Halftime Winner'] != 'Draw'),
    1, 0)
print(df.columns)

# Slice the data were need from the file
precovid_results = df.iloc[10044:10332]
postcovid_results = df.iloc[10332:]
precovid_results['Season'].replace({'2019-20': 'Pre-Covid'}, inplace=True)
postcovid_results['Season'].replace({'2019-20': 'Post-Covid', '2020-21': 'Post-Covid'}, inplace=True)

# check head and tail of new dataframes
print(precovid_results.head())
print(precovid_results.tail())
print(postcovid_results.head())
print(postcovid_results.tail())

# Get some overall statistics on the data
print(precovid_results.describe())
print(postcovid_results.describe())

# Pre covid Home goals
precovid_data1 = precovid_results.groupby('Season')['FTHG'].sum()
precovid_data1 = pd.DataFrame(precovid_data1)
precovid_data1.columns = ['Home Goals']

# Pre covid Away goals
precovid_data2 = precovid_results.groupby('Season')['FTAG'].sum()
precovid_data2 = pd.DataFrame(precovid_data2)
precovid_data2.columns = ['Away Goals']

# Pre covid Comebacks
precovid_data3 = precovid_results.groupby('Season')['Comeback'].sum()
precovid_data3 = pd.DataFrame(precovid_data3)
precovid_data3.columns = ['Comebacks']

# Number of Games
precovid_data4 = precovid_results.groupby('Season')['Season'].count()
precovid_data4 = pd.DataFrame(precovid_data4)
precovid_data4.columns = ['Games']

# Yellow Cards
precovid_data5 = precovid_results.groupby('Season')['Total Yellow cards'].sum()
precovid_data5 = pd.DataFrame(precovid_data5)
precovid_data5.columns = ['Total Yellow Cards']

# Red Cards
precovid_data6 = precovid_results.groupby('Season')['Total Red cards'].sum()
precovid_data6 = pd.DataFrame(precovid_data6)
precovid_data6.columns = ['Total Red Cards']

# Mergeing the Dataframes
precovid_data1 = precovid_data1.merge(precovid_data2, on='Season', how='left')
precovid_data1 = pd.merge(precovid_data1, precovid_data3, on='Season', how='left')
precovid_data1 = pd.merge(precovid_data1, precovid_data4, on='Season', how='left')
precovid_data1 = pd.merge(precovid_data1, precovid_data5, on='Season', how='left')
precovid_data1 = pd.merge(precovid_data1, precovid_data6, on='Season', how='left')
print(precovid_data1)

# Post covid Home goals
postcovid_data1 = postcovid_results.groupby('Season')['FTHG'].sum()
postcovid_data1 = pd.DataFrame(postcovid_data1)
postcovid_data1.columns = ['Home Goals']

# Post covid Away goals
postcovid_data2 = postcovid_results.groupby('Season')['FTAG'].sum()
postcovid_data2 = pd.DataFrame(postcovid_data2)
postcovid_data2.columns = ['Away Goals']

# Post covid Comebacks
postcovid_data3 = postcovid_results.groupby('Season')['Comeback'].sum()
postcovid_data3 = pd.DataFrame(postcovid_data3)
postcovid_data3.columns = ['Comebacks']

# Number of Games
postcovid_data4 = postcovid_results.groupby('Season')['Season'].count()
postcovid_data4 = pd.DataFrame(postcovid_data4)
postcovid_data4.columns = ['Games']

# Yellow Cards
postcovid_data5 = postcovid_results.groupby('Season')['Total Yellow cards'].sum()
postcovid_data5 = pd.DataFrame(postcovid_data5)
postcovid_data5.columns = ['Total Yellow Cards']

# Red Cards
postcovid_data6 = postcovid_results.groupby('Season')['Total Red cards'].sum()
postcovid_data6 = pd.DataFrame(postcovid_data6)
postcovid_data6.columns = ['Total Red Cards']

# Mergeing the Dataframes
postcovid_data1 = postcovid_data1.merge(postcovid_data2, on='Season', how='left')
postcovid_data1 = pd.merge(postcovid_data1, postcovid_data3, on='Season', how='left')
postcovid_data1 = pd.merge(postcovid_data1, postcovid_data4, on='Season', how='left')
postcovid_data1 = pd.merge(postcovid_data1, postcovid_data5, on='Season', how='left')
postcovid_data1 = pd.merge(postcovid_data1, postcovid_data6, on='Season', how='left')
print(postcovid_data1)

# Joining the dataframes
Covid_Season = pd.concat([precovid_data1, postcovid_data1])
print(Covid_Season)

# Average number of Home and away goals
Covid_Season['Average Home goals'] = Covid_Season['Home Goals'] / Covid_Season['Games']
Covid_Season['Average Away goals'] = Covid_Season['Away Goals'] / Covid_Season['Games']

# Average Number of Red and Yellow Cards
Covid_Season['Average Yellow Cards'] = Covid_Season['Total Yellow Cards'] / Covid_Season['Games']
Covid_Season['Average Red Cards'] = Covid_Season['Total Red Cards'] / Covid_Season['Games']

#Produce bar charts to represent the data
plt.style.use('seaborn-whitegrid')
fig, ax= plt.subplots()
ax.bar(Covid_Season.index,Covid_Season['Average Home goals'], color='maroon')
ax.set_title('Average Home Goals scored')
ax.set_ylabel('Number of goals', rotation=90)

fig, ax= plt.subplots()
ax.bar(Covid_Season.index,Covid_Season['Average Away goals'],color='maroon')
ax.set_title('Average Away Goals scored')
ax.set_ylabel('Number of goals', rotation=90)

fig, ax= plt.subplots()
ax.bar(Covid_Season.index,Covid_Season['Average Yellow Cards'],color='maroon')
ax.set_title('Average Yellow cards')
ax.set_ylabel('Number of cards', rotation=90)

fig, ax= plt.subplots()
ax.bar(Covid_Season.index,Covid_Season['Average Red Cards'],color='maroon')
ax.set_title('Average Red cards')
ax.set_ylabel('Number of cards', rotation=90)

fig, ax= plt.subplots()
ax.bar(Covid_Season.index,Covid_Season['Comebacks'],color='maroon')
ax.set_title('Comebacks')
ax.set_ylabel('Number of Comebacks', rotation=90)
plt.show()

### Pre covid Home results by team

# Number Games by team
home_gamesprec = precovid_results.groupby('HomeTeam')['HomeTeam'].count()
home_gamesprec = pd.DataFrame(home_gamesprec)
home_gamesprec.columns = ['Games']

#Add a column to show the Season
home_gamesprec['Season']='Precovid'

# Number Goals scored by Home team
home_gamesprec1 = precovid_results.groupby('HomeTeam')['FTHG'].sum()
home_gamesprec1 = pd.DataFrame(home_gamesprec1)
home_gamesprec1.columns = ['Goals Scored']

# NumberGoals conceded by Home team
home_gamesprec2 = precovid_results.groupby('HomeTeam')['FTAG'].sum()
home_gamesprec2 = pd.DataFrame(home_gamesprec2)
home_gamesprec2.columns = ['Goals Conceded']

# Merging dataframes
home_gamesprec = home_gamesprec.merge(home_gamesprec1, how='left', on='HomeTeam')
home_gamesprec = home_gamesprec.merge(home_gamesprec2, how='left', on='HomeTeam')

###Pre Covid awayprec results by team

# Games by team
away_gamesprec = precovid_results.groupby('AwayTeam')['AwayTeam'].count()
away_gamesprec= pd.DataFrame(away_gamesprec)
away_gamesprec.columns = ['Games']

#Add a column to show the Season
away_gamesprec['Season']='Precovid'

# Goals scored by Away team
away_gamesprec1 = precovid_results.groupby('AwayTeam')['FTAG'].sum()
away_gamesprec1 = pd.DataFrame(away_gamesprec1)
away_gamesprec1.columns = ['Goals Scored']

# Goals conceded by Away team
away_gamesprec2 = precovid_results.groupby('AwayTeam')['FTHG'].sum()
away_gamesprec2 = pd.DataFrame(away_gamesprec2)
away_gamesprec2.columns = ['Goals Conceded']

# Merging dataframes
away_gamesprec = away_gamesprec.merge(away_gamesprec1, how='left', on='AwayTeam')
away_gamesprec = away_gamesprec.merge(away_gamesprec2, how='left', on='AwayTeam')

### Post covid Home results by team

# Number Games by team
home_gamespostc = postcovid_results.groupby('HomeTeam')['HomeTeam'].count()
home_gamespostc = pd.DataFrame(home_gamespostc)
home_gamespostc.columns = ['Games']

#Add a column to show the Season
home_gamespostc['Season']='Postcovid'

# Number of Goals scored by Home team
home_gamespostc1 = postcovid_results.groupby('HomeTeam')['FTHG'].sum()
home_gamespostc1 = pd.DataFrame(home_gamespostc1)
home_gamespostc1.columns = ['Goals Scored']

# Number of Goals conceded by Home team
home_gamespostc2 = postcovid_results.groupby('HomeTeam')['FTAG'].sum()
home_gamespostc2 = pd.DataFrame(home_gamespostc2)
home_gamespostc2.columns = ['Goals Conceded']

# Merging dataframes
home_gamespostc = home_gamespostc.merge(home_gamespostc1, how='left', on='HomeTeam')
home_gamespostc = home_gamespostc.merge(home_gamespostc2, how='left', on='HomeTeam')

###Post Covid awayprec results by team

# Games by team
away_gamespostc = postcovid_results.groupby('AwayTeam')['AwayTeam'].count()
away_gamespostc = pd.DataFrame(away_gamespostc)
away_gamespostc.columns = ['Games']

#Add a column to show the Season
away_gamespostc['Season']='Postcovid'

# Goals scored by away team
away_gamespostc1 = postcovid_results.groupby('AwayTeam')['FTAG'].sum()
away_gamespostc1 = pd.DataFrame(away_gamespostc1)
away_gamespostc1.columns = ['Goals Scored']

# Goals conceded by away team
away_gamespostc2 = postcovid_results.groupby('AwayTeam')['FTHG'].sum()
away_gamespostc2 = pd.DataFrame(away_gamespostc2)
away_gamespostc2.columns = ['Goals Conceded']

# Merging dataframes
away_gamespostc = away_gamespostc.merge(away_gamespostc1, how='left', on='AwayTeam')
away_gamespostc = away_gamespostc.merge(away_gamespostc2, how='left', on='AwayTeam')

#Merge the resulting dataframes
covid_season_home= pd.concat([home_gamesprec,home_gamespostc])
covid_season_home.sort_values(['HomeTeam', 'Season'], ascending=(True,True), inplace=True)
covid_season_home=covid_season_home.reset_index(drop=False)

covid_season_away= pd.concat([away_gamesprec,away_gamespostc])
covid_season_away.sort_values(['AwayTeam','Season'], ascending=(True,True), inplace=True)
covid_season_away=covid_season_away.reset_index(drop=False)

#Remove teams that we only have 1 value for
covid_season_home=covid_season_home.set_index('HomeTeam')
covid_season_home=covid_season_home.drop(['Fulham','Leeds','West Brom'],axis=0)
covid_season_away=covid_season_away.set_index('AwayTeam')
covid_season_away=covid_season_away.drop(['Fulham','Leeds','West Brom'],axis=0)

#reorder the columns
column_order=['Season','Games','Goals Scored','Goals Conceded']
covid_season_home=covid_season_home.reindex(columns=column_order)
covid_season_away=covid_season_away.reindex(columns=column_order)

print(covid_season_home)
print(covid_season_away)

#Create columns for the average number of goals scored and conceded
covid_season_home['Average number of goals scored']=covid_season_home['Goals Scored']/covid_season_home['Games']
covid_season_home['Average number of goals conceded']= covid_season_home['Goals Conceded']/covid_season_home['Games']
covid_season_away['Average number of goals scored']=covid_season_away['Goals Scored']/covid_season_away['Games']
covid_season_away['Average number of goals conceded']= covid_season_away['Goals Conceded']/covid_season_away['Games']

#Create barcharts to visualise the data
sns.set_style("whitegrid")
sns.set_palette('bright')
covid_season_home.sort_values(by=['Goals Scored'], inplace=True, ascending=False)
sns.barplot(x='Goals Scored', y='HomeTeam',hue='Season', data=covid_season_home.reset_index())
plt.ylabel("Team", rotation=90, fontsize=10)
plt.title("Total Goals Scored Pre & Post Covid at home", fontsize=15)
plt.show()

covid_season_away.sort_values(by=['Goals Scored'], inplace=True, ascending=False)
sns.barplot(x='Goals Scored', y='AwayTeam',hue='Season', data=covid_season_away.reset_index())
plt.ylabel("Team", rotation=90, fontsize=10)
plt.title("Total Goals Scored Pre & Post Covid away from home", fontsize=15)
plt.show()

covid_season_home.sort_values(by=['Goals Conceded'], inplace=True, ascending=False)
sns.barplot(x='Goals Conceded', y='HomeTeam',hue='Season', data=covid_season_home.reset_index())
plt.ylabel("Team", rotation=90, fontsize=10)
plt.title("Total Goals conceded Pre & Post Covid at home", fontsize=15)
plt.show()

covid_season_away.sort_values(by=['Goals Conceded'], inplace=True, ascending=False)
sns.barplot(x='Goals Conceded', y='AwayTeam',hue='Season', data=covid_season_away.reset_index())
plt.ylabel('Team', rotation=90, fontsize=10)
plt.title("Total Goals conceded Pre & Post Covid away from home", fontsize=15)
plt.show()

covid_season_home.sort_values(by=['Average number of goals scored'], inplace=True, ascending=False)
sns.barplot(x='HomeTeam', y='Average number of goals scored' ,hue='Season', data=covid_season_home.reset_index())
plt.xticks(rotation=30, fontsize=8)
plt.xlabel('Team', fontsize= 10)
plt.ylabel("Goals", rotation=90, fontsize=10)
plt.title('Average No of goals scored at home Pre & Post Covid', fontsize=15)
plt.show()

covid_season_home.sort_values(by=['Average number of goals conceded'], inplace=True, ascending=False)
sns.barplot(x='HomeTeam', y='Average number of goals conceded',hue='Season', data=covid_season_home.reset_index())
plt.xticks(rotation=30, fontsize=8)
plt.xlabel('Team', fontsize= 10)
plt.ylabel("Goals", rotation=90, fontsize=10)
plt.title('Average No of goals conceded at home Pre & Post Covid', fontsize=15)
plt.show()

covid_season_away.sort_values(by=['Average number of goals scored'], inplace=True, ascending=False)
sns.barplot(x='AwayTeam', y='Average number of goals scored' ,hue='Season', data=covid_season_away.reset_index())
plt.xticks(rotation=30, fontsize=8)
plt.xlabel('Team',fontsize= 10)
plt.ylabel("Goals", rotation=90, fontsize=10)
plt.title('Average No of goals scored away from home Pre & Post Covid', fontsize=15)
plt.show()

covid_season_away.sort_values(by=['Average number of goals conceded'], inplace=True, ascending=False)
sns.barplot(x='AwayTeam', y='Average number of goals conceded' ,hue='Season', data=covid_season_away.reset_index())
plt.xticks(rotation=30, fontsize=8)
plt.xlabel('Team',fontsize= 10)
plt.ylabel("Goals", rotation=90, fontsize=10)
plt.title('Average No of goals conceded away from home Pre & Post Covid', fontsize=15)
plt.show()
