import numpy as np
import pandas as pd
import pickle

file="P87-S2-Dataset-Basics-Resources\heart.csv"

# load file using pandas
set = pd.read_csv(file)
print(set.head())

# load file using numpy
npdata= np.loadtxt(file, delimiter=",", skiprows=1)
print(npdata)