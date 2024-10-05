import requests

upload_url = 'http://127.0.0.1:5000/upload-file'
review_url = 'http://127.0.0.1:5000/review'

def upload_file(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(upload_url, files=files)

    if response.status_code == 200:
        print('File uploaded successfully:', response.json())
    else:
        print('Failed to upload file:', response.json())

def analyze_review(review_text):
    data = {'review': review_text}
    response = requests.post(review_url, data=data)

    if response.status_code == 200:
        print('Sentiment analysis result:', response.json())
    else:
        print('Failed to analyze review:', response.json())

# Example Usage:
file_path = 'path_to_your_file/customer_reviews.xlsx'  
review_text = 'This is a fantastic product! Highly recommend it.'

upload_file(file_path)
analyze_review(review_text)
