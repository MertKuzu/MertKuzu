import pandas as pd

data = pd.read_csv("25.2_nba.csv")

df = pd.DataFrame(data)

result = df

result = df.head(10)

result = len(df.index)

result = df["Salary"].mean()

result = df["Salary"].max()

result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]

result = df[(df["Age"] <=25) & (df["Age"] >= 20)][["Name","Team","Age"]].sort_values("Age",ascending=False)

result = df[df["Name"] == "John Holland"][["Name","Team"]]

result = df.groupby("Team")["Salary"].mean()

result = len(df.groupby("Team"))

result = df["Team"].nunique()

# for i in df["Name"]:
#     if "and" in str(i):
#         print(i)
#     else:
#         pass


print(result)