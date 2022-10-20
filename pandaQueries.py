import pandas as pd

file = "P87-S2-Dataset-Basics-Resources\heart.csv"

# load file using pandas
set = pd.read_csv(file)

print("\n")
print("All males in the file")
print(set.query('sex==1'))

print("\n")
print("List of all people over 45 years old is saved in QueriesOutput\AllOver45.xlsx")
set.query('age>45').to_excel("QueriesOutput\AllOver45.xlsx")
