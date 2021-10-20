import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns=["Column 1","Column 2", "Column 3"])

result = df
result = df["Column 1"]
result = type(df["Column 1"])
result = df[["Column 1", "Column 2"]]

# loc["row","column"] => loc["row"] => loc[:,"column"]

result = df.loc["A"]
result = type(df.loc["A"])
result = df.loc[:,"Column 1"]
result = df.loc[:,["Column 1","Column 2"]]
result = df.loc[:,"Column 1":"Column 3"]
result = df.loc[:,:"Column 3"]
result = df.loc["A":"B",:"Column 2"]
result = df.loc[:"B",:"Column 2"]
result = df.iloc[1]
result = df.loc["A","Column 2"]
result = df.loc["C", "Column 1"]
result = df.loc[["A","B"],["Column 2","Column 3"]]

df["Column 4"] = pd.Series(randn(3), ["A","B","C"])
df["Column 5"] = df["Column 1"] + df["Column 3"]

df.drop("Column 5", axis=1 , inplace=True)   #inplace: this is replacing copy to original

print(df)

print(result)