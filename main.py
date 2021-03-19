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

# Make a column for total goals scored
df['Goals Scored'] = df['FTHG'] + df['FTAG']

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
df['Final Loser'] = np.select(conditions1, values3, default='Draw')

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

# Pre covid Total scores
precovid_data = precovid_results.groupby('Season')['Goals Scored'].sum()
precovid_data = pd.DataFrame(precovid_data)
precovid_data.columns = ['Total Goals']

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
precovid_data = precovid_data1.merge(precovid_data2, on='Season', how='left')
precovid_data = pd.merge(precovid_data, precovid_data3, on='Season', how='left')
precovid_data = pd.merge(precovid_data, precovid_data4, on='Season', how='left')
precovid_data = pd.merge(precovid_data, precovid_data5, on='Season', how='left')
precovid_data = pd.merge(precovid_data, precovid_data6, on='Season', how='left')
print(precovid_data)

# Post covid Total scores
postcovid_data = postcovid_results.groupby('Season')['Goals Scored'].sum()
postcovid_data = pd.DataFrame(postcovid_data)
postcovid_data.columns = ['Total Goals']

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
postcovid_data = postcovid_data1.merge(postcovid_data2, on='Season', how='left')
postcovid_data = pd.merge(postcovid_data, postcovid_data3, on='Season', how='left')
postcovid_data = pd.merge(postcovid_data, postcovid_data4, on='Season', how='left')
postcovid_data = pd.merge(postcovid_data, postcovid_data5, on='Season', how='left')
postcovid_data = pd.merge(postcovid_data, postcovid_data6, on='Season', how='left')
print(postcovid_data)

# Joining the dataframes
Covid_Season = pd.concat([precovid_data, postcovid_data])
print(Covid_Season)

# Average nunber of Home and awayprec goals
Covid_Season['Average Home goals'] = Covid_Season['Home Goals'] / Covid_Season['Games']
Covid_Season['Average Away goals'] = Covid_Season['Away Goals'] / Covid_Season['Games']

# Average Number of Red and Yellow Cards
Covid_Season['Average Yellow goals'] = Covid_Season['Total Yellow Cards'] / Covid_Season['Games']
Covid_Season['Average Red goals'] = Covid_Season['Total Red Cards'] / Covid_Season['Games']
print(Covid_Season)

### Pre covid Home results by team
homeprecovid = precovid_results.copy()

# Number Games by team
home_gamesprec = precovid_results.groupby('HomeTeam')['HomeTeam'].count()
home_gamesprec = pd.DataFrame(home_gamesprec)
home_gamesprec.columns = ['Games']

# Number Goals scored by team
home_gamesprec1 = precovid_results.groupby('HomeTeam')['FTHG'].sum()
home_gamesprec1 = pd.DataFrame(home_gamesprec1)
home_gamesprec1.columns = ['Goals Scored']

# NumberGoals against by team
home_gamesprec2 = precovid_results.groupby('HomeTeam')['FTAG'].sum()
home_gamesprec2 = pd.DataFrame(home_gamesprec2)
home_gamesprec2.columns = ['Goals Against']

# Comebacks by team
homeprecovid['trailer'] = np.where((homeprecovid['HomeTeam'] == homeprecovid['Final Winner'])&(homeprecovid['Comeback']== 1),1, 0)
home_gamesprec3 = homeprecovid.groupby('HomeTeam')['trailer'].sum()
home_gamesprec3 = pd.DataFrame(home_gamesprec3
                               )
home_gamesprec3.columns = ['Comeback']

# Wins by team
homeprecovid['HomeTeam'] = homeprecovid['HomeTeam'].astype('category')
home_gamesprec4 = homeprecovid[homeprecovid['Final Winner'] == homeprecovid['HomeTeam']].groupby(['HomeTeam']).size().reset_index(name='Wins')

# Loss by team
home_gamesprec5 = homeprecovid[homeprecovid['Final Winner'] == homeprecovid['AwayTeam']].groupby(['HomeTeam']).size().reset_index(name='Loss')

# Draws by team
home_gamesprec6 = homeprecovid[homeprecovid['Final Winner'] == 'Draw'].groupby(['HomeTeam']).size().reset_index(name='Draws')

# Merging dataframes
home_gamesprec = home_gamesprec.merge(home_gamesprec1, how='left', on='HomeTeam')
home_gamesprec = home_gamesprec.merge(home_gamesprec2, how='left', on='HomeTeam')
home_gamesprec = home_gamesprec.merge(home_gamesprec3, how='left', on='HomeTeam')
home_gamesprec = home_gamesprec.merge(home_gamesprec4, how='left', on='HomeTeam')
home_gamesprec = home_gamesprec.merge(home_gamesprec5, how='left', on='HomeTeam')
home_gamesprec = home_gamesprec.merge(home_gamesprec6, how='left', on='HomeTeam')

# Goals scored per game
home_gamesprec['Goals scored per game'] = round(home_gamesprec['Goals Scored']/home_gamesprec['Games'],2)

# Goals against per game
home_gamesprec['Goals against per game'] = round(home_gamesprec['Goals Against']/home_gamesprec['Games'],2)

# Create 'Proportion Wins' column
home_gamesprec['% Wins'] = 100*round(home_gamesprec['Wins']/home_gamesprec['Games'],3)

# Create 'Proportion Loss' column
home_gamesprec['% Loss'] = 100*round(home_gamesprec['Loss']/home_gamesprec['Games'],3)

# Create 'Proportion Draws' column
home_gamesprec['% Draws'] = 100*round(home_gamesprec['Draws']/home_gamesprec['Games'],3)

# Create 'Aprov' column
home_gamesprec['% Points Performance'] = 100*round((3*home_gamesprec['Wins']+home_gamesprec['Draws'])/(3*home_gamesprec['Games']),3)

###Pre Covid awayprec results by team
awayprec = precovid_results.copy()

# Games by team
away_gamesprec = precovid_results.groupby('AwayTeam')['AwayTeam'].count()
away_gamesprec= pd.DataFrame(away_gamesprec)
away_gamesprec.columns = ['Games']

# Goals scored by team
away_gamesprec1 = precovid_results.groupby('AwayTeam')['FTAG'].sum()
away_gamesprec1 = pd.DataFrame(away_gamesprec1)
away_gamesprec1.columns = ['Goals Scored']

# Goals against by team
away_gamesprec2 = precovid_results.groupby('AwayTeam')['FTHG'].sum()
away_gamesprec2 = pd.DataFrame(away_gamesprec2)
away_gamesprec2.columns = ['Goals Against']

# Comebacks by team
awayprec['trailer'] = np.where((awayprec['AwayTeam'] == awayprec['Final Winner']) & (awayprec['Comeback'] == 1), 1, 0)
away_gamesprec3 = awayprec.groupby('AwayTeam')['trailer'].sum()
away_gamesprec3 = pd.DataFrame(away_gamesprec3)
away_gamesprec3.columns = ['Comeback']

# Wins by team
awayprec['AwayTeam'] = awayprec['AwayTeam'].astype('category')
away_gamesprec4 = awayprec[awayprec['Final Winner'] == awayprec['AwayTeam']].groupby(['AwayTeam']).size().reset_index(name='Wins')

# Loss by team
away_gamesprec5 = awayprec[awayprec['Final Winner'] == awayprec['HomeTeam']].groupby(['AwayTeam']).size().reset_index(name='Loss')

# Draws by team
away_gamesprec6 = awayprec[awayprec['Final Winner'] == 'Draw'].groupby(['AwayTeam']).size().reset_index(name='Draws')

# Merging dataframes
away_gamesprec = away_gamesprec.merge(away_gamesprec1, how='left', on='AwayTeam')
away_gamesprec = away_gamesprec.merge(away_gamesprec2, how='left', on='AwayTeam')
away_gamesprec = away_gamesprec.merge(away_gamesprec3, how='left', on='AwayTeam')
away_gamesprec = away_gamesprec.merge(away_gamesprec4, how='left', on='AwayTeam')
away_gamesprec = away_gamesprec.merge(away_gamesprec5, how='left', on='AwayTeam')
away_gamesprec = away_gamesprec.merge(away_gamesprec6, how='left', on='AwayTeam')

# Goals scored per game
away_gamesprec['Goals scored per game'] = round(away_gamesprec['Goals Scored']/away_gamesprec['Games'],2)

# Goals against per game
away_gamesprec['Goals against per game'] = round(away_gamesprec['Goals Against']/away_gamesprec['Games'],2)

# Create 'Proportion Wins' column
away_gamesprec['% Wins'] = 100*round(away_gamesprec['Wins']/away_gamesprec['Games'],3)

# Create 'Proportion Loss' column
away_gamesprec['% Loss'] = 100*round(away_gamesprec['Loss']/away_gamesprec['Games'],3)

# Create 'Proportion Draws' column
away_gamesprec['% Draws'] = 100*round(away_gamesprec['Draws']/away_gamesprec['Games'],3)

# Create 'Aprov' column
away_gamesprec['% Points Performance'] = 100*round((3*away_gamesprec['Wins']+away_gamesprec['Draws'])/(3*away_gamesprec['Games']),3)

### Post covid Home results by team
homepostcovid = postcovid_results.copy()

# Number Games by team
home_gamespostc = postcovid_results.groupby('HomeTeam')['HomeTeam'].count()
home_gamespostc = pd.DataFrame(home_gamespostc)
home_gamespostc.columns = ['Games']

# Number Goals scored by team
home_gamespostc1 = postcovid_results.groupby('HomeTeam')['FTHG'].sum()
home_gamespostc1 = pd.DataFrame(home_gamespostc1)
home_gamespostc1.columns = ['Goals Scored']

# NumberGoals against by team
home_gamespostc2 = postcovid_results.groupby('HomeTeam')['FTAG'].sum()
home_gamespostc2 = pd.DataFrame(home_gamespostc2)
home_gamespostc2.columns = ['Goals Against']

# Comebacks by team
homepostcovid['trailer'] = np.where((homepostcovid['HomeTeam'] == homepostcovid['Final Winner'])&(homepostcovid['Comeback']== 1),1, 0)
home_gamespostc3 = homepostcovid.groupby('HomeTeam')['trailer'].sum()
home_gamespostc3 = pd.DataFrame(home_gamespostc3)
home_gamespostc3.columns = ['Comeback']

# Wins by team
homepostcovid['HomeTeam'] = homepostcovid['HomeTeam'].astype('category')
home_gamespost4 = homepostcovid[homepostcovid['Final Winner'] == homepostcovid['HomeTeam']].groupby(['HomeTeam']).size().reset_index(name='Wins')

# Loss by team
home_gamespostc5 = homepostcovid[homepostcovid['Final Winner'] == homepostcovid['AwayTeam']].groupby(['HomeTeam']).size().reset_index(name='Loss')

# Draws by team
home_gamespostc6 = homepostcovid[homepostcovid['Final Winner'] == 'Draw'].groupby(['HomeTeam']).size().reset_index(name='Draws')

# Merging dataframes
home_gamespostc = home_gamespostc.merge(home_gamespostc1, how='left', on='HomeTeam')
home_gamespostc = home_gamespostc.merge(home_gamespostc2, how='left', on='HomeTeam')
home_gamespostc = home_gamespostc.merge(home_gamespostc3, how='left', on='HomeTeam')
home_gamespostc = home_gamespostc.merge(home_gamespost4, how='left', on='HomeTeam')
home_gamespostc = home_gamespostc.merge(home_gamespostc5, how='left', on='HomeTeam')
home_gamespostc = home_gamespostc.merge(home_gamespostc6, how='left', on='HomeTeam')

# Goals scored per game
home_gamespostc['Goals scored per game'] = round(home_gamespostc['Goals Scored'] / home_gamespostc['Games'], 2)

# Goals against per game
home_gamespostc['Goals against per game'] = round(home_gamespostc['Goals Against'] / home_gamespostc['Games'], 2)

# Create 'Proportion Wins' column
home_gamespostc['% Wins'] = 100 * round(home_gamespostc['Wins'] / home_gamespostc['Games'], 3)

# Create 'Proportion Loss' column
home_gamespostc['% Loss'] = 100 * round(home_gamespostc['Loss'] / home_gamespostc['Games'], 3)

# Create 'Proportion Draws' column
home_gamespostc['% Draws'] = 100 * round(home_gamespostc['Draws'] / home_gamespostc['Games'], 3)

# Create 'Aprov' column
home_gamespostc['% Points Performance'] = 100 * round((3 * home_gamespostc['Wins'] + home_gamespostc['Draws']) / (3 * home_gamespostc['Games']), 3)

###Post Covid awayprec results by team
awaypostcovid= postcovid_results.copy()

# Games by team
away_gamespostc = postcovid_results.groupby('AwayTeam')['AwayTeam'].count()
away_gamespostc = pd.DataFrame(away_gamespostc)
away_gamespostc.columns = ['Games']

# Goals scored by team
away_gamespostc1 = postcovid_results.groupby('AwayTeam')['FTAG'].sum()
away_gamespostc1 = pd.DataFrame(away_gamespostc1)
away_gamespostc1.columns = ['Goals Scored']

# Goals against by team
away_gamespostc2 = postcovid_results.groupby('AwayTeam')['FTHG'].sum()
away_gamespostc2 = pd.DataFrame(away_gamesprec2)
away_gamespostc2.columns = ['Goals Against']

# Comebacks by team
awaypostcovid['trailer'] = np.where((awaypostcovid['AwayTeam'] == awaypostcovid['Final Winner'])&(awaypostcovid['Comeback']== 1),1, 0)
away_gamespostc3 = awaypostcovid.groupby('AwayTeam')['trailer'].sum()
away_gamespostc3 = pd.DataFrame(away_gamesprec3)
away_gamespostc3.columns = ['Comeback']

# Wins by team
awaypostcovid['AwayTeam'] = awaypostcovid['AwayTeam'].astype('category')
away_gamespostc4 = awaypostcovid[awaypostcovid['Final Winner'] == awaypostcovid['AwayTeam']].groupby(['AwayTeam']).size().reset_index(name='Wins')

# Loss by team
away_gamespostc5 = awaypostcovid[awaypostcovid['Final Winner'] == awaypostcovid['HomeTeam']].groupby(['AwayTeam']).size().reset_index(name='Loss')

# Draws by team
away_gamespostc6 = awaypostcovid[awaypostcovid['Final Winner'] == 'Draw'].groupby(['AwayTeam']).size().reset_index(name='Draws')

# Merging dataframes
away_gamespostc = away_gamespostc.merge(away_gamespostc1, how='left', on='AwayTeam')
away_gamespostc = away_gamespostc.merge(away_gamespostc2, how='left', on='AwayTeam')
away_gamespostc = away_gamespostc.merge(away_gamespostc3, how='left', on='AwayTeam')
away_gamespostc = away_gamespostc.merge(away_gamespostc4, how='left', on='AwayTeam')
away_gamespostc = away_gamespostc.merge(away_gamespostc5, how='left', on='AwayTeam')
away_gamespostc = away_gamespostc.merge(away_gamespostc6, how='left', on='AwayTeam')

# Goals scored per game
away_gamespostc['Goals scored per game'] = round(away_gamespostc['Goals Scored'] / away_gamespostc['Games'], 2)

# Goals against per game
away_gamespostc['Goals against per game'] = round(away_gamespostc['Goals Against'] / away_gamespostc['Games'], 2)

# Create 'Proportion Wins' column
away_gamespostc['% Wins'] = 100 * round(away_gamespostc['Wins'] / away_gamespostc['Games'], 3)

# Create 'Proportion Loss' column
away_gamespostc['% Loss'] = 100 * round(away_gamespostc['Loss'] / away_gamespostc['Games'], 3)

# Create 'Proportion Draws' column
away_gamespostc['% Draws'] = 100 * round(away_gamespostc['Draws'] / away_gamespostc['Games'], 3)

# Create 'Aprov' column
away_gamespostc['% Points Performance'] = 100 * round((3 * away_gamespostc['Wins'] + away_gamespostc['Draws']) / (3 * away_gamespostc['Games']), 3)

print(home_gamesprec.head())
print(away_gamesprec.head())
print(home_gamespostc.head())
print(away_gamespostc.head())