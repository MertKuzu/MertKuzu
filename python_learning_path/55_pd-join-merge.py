import pandas as pd 

# customers = {
#     "CustomerID":[1,2,3,4],
#     "FirstName":["Ahmet","Ali","Hasan","Canan"],
#     "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     "OrderID":[10,11,12,13],
#     "CustomerID":[1,2,5,7],
#     "OrderDate":["2010-07-04","2010-08-04","2010-07-07","2012-07-04"]
# }

# df_customers = pd.DataFrame(customers, columns=["CustomerID","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns=["OrderID","CustomerID","OrderDate"])


# print(df_customers)
# print(df_orders)


# result = pd.merge(df_customers,df_orders, how="inner")
# result = pd.merge(df_customers,df_orders, how="outer")

customersA = {
    "CustomerID":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerID":[1,2,3,4],
    "FirstName":["Yağmur","Çınar","Cengiz","Can"],
    "LastName":["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns=["CustomerID","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerID","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])
result = pd.concat([df_customersA,df_customersB], axis=1)

print(result)