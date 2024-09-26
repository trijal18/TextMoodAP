import pandas as pd
from model import analyze_sentiment

df=pd.read_excel(r"C:\Users\admin\Downloads\customer_reviews.xlsx")

reviews_list=[]
for review in df["Review"]:
    reviews_list.append(str(review))

response=analyze_sentiment(reviews_list)
print(type(response))
print(response)