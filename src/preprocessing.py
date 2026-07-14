import os
import pandas as pd

csv_path = os.path.join(
    os.path.dirname(__file__) ,
    ".." ,
    "dataset" ,
    "winequality-red.csv"
)

df = pd.read_csv(csv_path , sep=";")

print(df)