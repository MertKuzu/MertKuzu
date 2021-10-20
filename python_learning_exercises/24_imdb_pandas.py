import pandas as pd


df = pd.read_csv("24.2_imdb_pandas.csv")

result = df
result = df.columns
result = df.info()

result = df.tail()
result = df.tail(10)

result = df["Movie_Title"]
result = df["Movie_Title"].head()
result = df[["Movie_Title","Rating"]].head()
result = df[["Movie_Title","Rating"]].tail(7)
result = df[5:10][["Movie_Title","Rating"]].head()
result = df[df["Rating"] >= 8][["Movie_Title","Rating"]].head(50)
result = df[(df["YR_Released"] <= 2015) & (df["YR_Released"] >= 2014)]["Movie_Title"]
result = df[(df["Num_Reviews"] >= 100000) | (df["Rating"] <= 9) & (df["Rating"] >= 8)]["Movie_Title"]


print(result)

