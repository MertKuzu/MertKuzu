import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ["Ahmet Yılmaz", "Can Ertük", "Hasan Korkmaz", "Cenk Saymaz", "Ali Turan", "Rıza Ertük", "Mustafa Can"],
    'Departman': ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "Bilgi İşlem"],
    'Yaş': [30, 25, 45, 50, 23, 34, 42],
    'Semt': ["Kadıköy", "Tuzla", "Maltepe", "Tuzla", "Kadıköy", "Maltepe", "Tuzla"],
    'Maaş': [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Bilgi İşlem")
result = df.groupby("Departman").sum()
result = df.groupby("Departman").mean()
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Yaş"].max()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]

result = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["Muhasebe"]





print(result)