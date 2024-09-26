from read_reviews import read_reviews

file_path = r"C:\Users\admin\Downloads\customer_reviews.xlsx"
response=read_reviews(file_path)
print(response)
print(type(response))