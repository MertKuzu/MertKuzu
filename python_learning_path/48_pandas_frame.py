import pandas as pd
from pandas.core.indexes.datetimes import date_range


list = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
dict_list = [
    {"Name":"Ahmet", "Grade":50,},
    {"Name":"Ali", "Grade":60,},
    {"Name":"Yağmur", "Grade":70,},
    {"Name":"Çınar", "Grade":80,}
    ]


df = pd.DataFrame()
df = pd.DataFrame([1,2,3,4])
df = pd.DataFrame(list, index = [1,2,3,4], columns=["Name","Orange"], dtype=float)
df = pd.DataFrame(dict)
df = pd.DataFrame(dict, index=["212","599","300","782"])
df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index=["210","320","599","720"])




# s1 = pd.Series([3,2,9,1])
# s2 = pd.Series([1,3,2,7])

# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

print(df)