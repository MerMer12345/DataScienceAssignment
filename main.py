import pandas as pd
df = pd.read_csv('dataset.csv')
countnull = df.isnull().sum()
print(countnull)
