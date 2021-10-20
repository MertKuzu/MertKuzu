import pandas as pd

df = pd.read_csv("49.2_pandas-file.csv")
df = pd.read_json("49.5_pandas-file.json", encoding="utf-8")


print(df)