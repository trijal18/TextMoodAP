import pandas as pd
from model import analyze_sentiment

class FileTypeNotSupportedException(Exception):
    """Custom exception for unsupported file types."""
    pass

def read_reviews(file_path):
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        raise FileTypeNotSupportedException("Unsupported file type. Please upload a .xlsx or .csv file.")

    if 'Review' not in df.columns:
        raise ValueError("The input file must contain a 'Review' column.")

    reviews_list = df["Review"].astype(str).tolist()
    # reviews_list=[]
    # for review in df['Review']:
    #     reviews_list.append(review)
    print(type(reviews_list))
    sentiments=analyze_sentiment(reviews_list)
    print(type(sentiments))
    return sentiments
# Example usage (assuming a valid file_path object):
file_path = r"C:\Users\admin\Downloads\customer_reviews.xlsx"  # Obtain the file path from the user or a web form
print(read_reviews(file_path))
