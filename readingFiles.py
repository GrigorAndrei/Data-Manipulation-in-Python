import numpy as np
import pandas as pd
import pickle

file="P87-S2-Dataset-Basics-Resources\heart.csv"

# load file using pandas
set = pd.read_csv(file)
print(set.head())

# load file using numpy
# Doeas not care for csv header
npdata= np.loadtxt(file, delimiter=",", skiprows=1)
print(npdata)

# Loading with genfromtxt to also get types and all values correctly
genText = np.genfromtxt(file, delimiter=",", dtype=None, names=True, encoding="utf-8-sig")
print(genText)
print(genText.dtype)

# Manual loading
def load_file(file):
    with open(file, encoding="utf-8-sig") as f:
        data, cols = [],[]
        for i,line in enumerate(f.read().splitlines()):
            if i == 0 :
                cols += line.split(",") # getting the head
            else:
                data.append([float(x) for x in line.split(",")]) # getting the actual values
        df=pd.DataFrame(data, columns=cols)
    return df

print(load_file(file).head())

