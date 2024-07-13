import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

users = pd.read_csv(r"C:\Users\manis\OneDrive\Desktop\CODSOFT\Users.csv.zip", dtype={'User-ID': int, 'Location': str, 'Age': float})
print(users)
books = pd.read_csv(r"C:\Users\manis\OneDrive\Desktop\CODSOFT\Books.csv.zip", dtype={'ISBN': str, 'Image-URL-L': str})
print(books)
print(books.head())

ratings = pd.read_csv(r"C:\Users\manis\OneDrive\Desktop\CODSOFT\Ratings.csv.zip", dtype={'User-ID': int, 'ISBN': str, 'Book-Rating': float})
print(ratings)
def preprocess_data(books, ratings):
    ratings_with_name = pd.merge(ratings, books, on='ISBN')
    ratings_with_name['Book-Rating'] = pd.to_numeric(ratings_with_name['Book-Rating'], errors='coerce')
    ratings_with_name.dropna(subset=['Book-Rating'], inplace=True)
    ratings_with_name = ratings_with_name[ratings_with_name['Book-Rating'] >= 0]
    ratings_with_name['User-Book'] = ratings_with_name['User-ID'].astype(str) + '-' + ratings_with_name['Book-Title']
    avg_rating_df = ratings_with_name.groupby('User-Book')['Book-Rating'].agg(lambda x: pd.to_numeric(x, errors='coerce').mean()).reset_index()
    return avg_rating_df

le = LabelEncoder()
final_ratings = preprocess_data(books, ratings)
encoded_final_ratings = final_ratings.copy()
encoded_final_ratings['User-Book'] = le.fit_transform(final_ratings['User-Book'])
encoded_final_ratings['Book-Rating'] = le.fit_transform(final_ratings['Book-Rating'])


def recommend(author_name, books, ratings):
    recommended_books = books[books['Book-Author'] == author_name]
    print(recommended_books)
    recommended_titles = recommended_books['Book-Title'].tolist()
    print(recommended_titles)
    merged_df = recommended_books.merge(ratings, on='ISBN')
    highly_rated_books = merged_df.sort_values('Book-Rating', ascending=False).head(10)
    return highly_rated_books

author_name = input("Enter the author's name: ")
recommended_titles = recommend(author_name, books, ratings)
print(recommended_titles)

