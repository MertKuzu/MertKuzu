# with open("28.5_files.txt", "r+", encoding="utf-8") as file:
#     file.seek(25)
#     file.write("deneme")

# with open("28.5_files.txt", "r+", encoding="utf-8") as file:
#     print(file.read())

# *********** Updating end of the page *********************

# with open("28.5_files.txt", "a", encoding="utf-8") as file:
#     file.write("\nUranium Kuzu")


#*********** Updating top of the page *************************


# with open("28.5_files.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Michael Scott\n"+content
#     file.seek(0)
#     file.write(content)




#************** Updating mid of the page *******************


with open("28.5_files.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(2, "Kuzu.da.bu\n")
    file.seek(0)

    # for i in list:
    #     file.write(i)

    #or

    file.writelines(list)



with open("28.5_files.txt", "r", encoding="utf-8") as file:
    print(file.read())
