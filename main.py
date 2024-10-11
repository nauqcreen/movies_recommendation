from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import scipy.sparse as sp
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Hàm get_data
def get_data():
    movie_data = pd.read_csv('/Users/dolphin/Downloads/movies_recommendation/data/movie_data.csv.zip')
    movie_data['original_title'] = movie_data['original_title'].str.lower()
    return movie_data

# Hàm combine_data
def combine_data(data):
    data_recommend = data.drop(columns=['movie_id', 'original_title', 'plot'])
    data_recommend['combine'] = data_recommend[data_recommend.columns[0:2]].apply(
        lambda x: ','.join(x.dropna().astype(str)), axis=1)
    data_recommend = data_recommend.drop(columns=['cast', 'genres'])
    return data_recommend

# Hàm transform_data
def transform_data(data_combine, data_plot):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(data_combine['combine'])
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data_plot['plot'])
    
    combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')
    cosine_sim = cosine_similarity(combine_sparse, combine_sparse)
    return cosine_sim

import ast  # Đảm bảo import ast ở đầu file

# Hàm recommend_movies với `ast.literal_eval` để chuyển đổi `Genres` thành danh sách
def recommend_movies(title, data, combine, transform):
    indices = pd.Series(data.index, index=data['original_title'])
    index = indices[title]
    
    sim_scores = list(enumerate(transform[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    
    movie_indices = [i[0] for i in sim_scores]
    
    movie_id = data['movie_id'].iloc[movie_indices]
    movie_title = data['original_title'].iloc[movie_indices]
    # Sử dụng `ast.literal_eval` để chuyển `Genres` từ chuỗi thành danh sách
    movie_genres = data['genres'].iloc[movie_indices].apply(ast.literal_eval)
    
    recommendation_data = pd.DataFrame(columns=['Movie_Id', 'Name', 'Genres'])
    recommendation_data['Movie_Id'] = movie_id.values
    recommendation_data['Name'] = movie_title.values
    recommendation_data['Genres'] = movie_genres.values
    
    return recommendation_data.to_dict(orient='records')

# Khởi tạo Flask
app = Flask(__name__)
CORS(app)

# Đọc dữ liệu và tính toán
data = get_data()
combine_data_result = combine_data(data)
cosine_sim_matrix = transform_data(combine_data_result, data[['plot']])

@app.route('/movie', methods=['GET'])
def recommend_movies_api():
    title = request.args.get('title')
    res = recommend_movies(title, data, combine_data_result, cosine_sim_matrix)
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)