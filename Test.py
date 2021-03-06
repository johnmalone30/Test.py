if __name__ == '__main__':
    print("Project Title")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
file = 'Premier league Covid football results.csv'
df = pd.read_csv(file)
#slice the data we need
results_data= df.iloc[10046:]
#print the head to ensure we've got the correct data
print(results_data.head())
