if __name__ == '__main__':
    print("Project Title")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
file = 'Premier league Covid football results.csv'
df = pd.read_csv(file)
print(df.head())
print(df.shape)
results_data= df[['Date','Time', 'HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR']]
print(results_data.head())
print(results_data.shape)
print(results_data.info())
print(results_data.isna().sum())
print(results_data.describe())
print(results_data['FTR'].value_counts())
pre_covid_data = results_data.iloc[:288]
post_covid_data = results_data.iloc[288:]
print(pre_covid_data.tail())
print(post_covid_data.head())
print(pre_covid_data.describe())
print(pre_covid_data['FTR'].value_counts())
print(post_covid_data.describe())
print(post_covid_data['FTR'].value_counts())
