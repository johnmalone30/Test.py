if __name__ == '__main__':
    print("Project Title")
import pandas as pd
file = 'Premier league Covid football results.csv'
df = pd.read_csv(file)
print(df.head())
