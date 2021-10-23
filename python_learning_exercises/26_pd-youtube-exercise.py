import pandas as pd

data = pd.read_csv("26.2_GBvideos.csv")

df = pd.DataFrame(data)

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)


# 2- İkinci 5 kaydı getiriniz.
result = df[5:].head()



# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)




# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1)




# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.

result = df["likes"].mean()
result = df["dislikes"].mean()



# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.

result = df[["likes","dislikes"]].head(50)




# 7- En çok görüntülenen video hangisidir ?

result = df[df["views"]==df["views"].max()][["title","views"]]



# 8- En düşük görüntülenen video hangisidir?

result = df[df["views"]==df["views"].min()][["title","views"]]



# 9- En fazla görüntülenen ilk 10 video hangisidir ?

result = df["views"].sort_values(ascending=False).head(10)



# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.

result = df.groupby("category_id")["likes"].mean()



# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

result = df.groupby("category_id").sum().sort_values("comment_count", ascending=False)



# 12- Her kategoride kaç video vardır ?

result = df.groupby("category_id")["title"].nunique()



# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

df["title_lenght"] = df["title"].apply(len)
result = df


# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

df["tag_number"] = df["tags"].apply(lambda x: len(x.split("|")))
result = df


# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

def percentageCalculate(dataset):

    likes = list(dataset["likes"])
    dislikes = list(dataset["dislikes"])

    listAll = list(zip(likes,dislikes))

    percantagelist = []

    for like,dislike in listAll:
        if (like+dislike) == 0:
            percantagelist.append(0)
        else:
            percantagelist.append(like/(like+dislike))

    return percantagelist

    

df["like_percentage"] = percentageCalculate(df)

print(df.sort_values("like_percentage", ascending=False)[["title","likes","dislikes","like_percentage"]])



#print(result)