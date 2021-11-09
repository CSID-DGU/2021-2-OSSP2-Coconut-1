import pandas as pd

data = pd.read_csv("./2021-2-OSSP2-Coconut-1/algorithm/matrix_231x201_211108.csv")
print(data.columns[0])
print(data.iloc[0]['region'])
print(len(data.columns)-1)
print(data.iloc[0][data.columns[0]])