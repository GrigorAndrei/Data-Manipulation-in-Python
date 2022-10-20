import pandas as pd

file = "Datasets\Astronauts.csv"

# load file using pandas
set = pd.read_csv(file)


print("\n")
print("All retired astronauts in the file")
print(set.query("SpaceWalks >20"))

# print("\n")
# print("List of all people over 45 years old is saved in QueriesOutput\AllOver45.xlsx")
# set.query('age>45').to_excel("QueriesOutput\AllOver45.xlsx")
