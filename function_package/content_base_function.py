from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
from pandas import isnull, notnull


def tfidf_matrix(movies):
    """
        Dùng hàm "TfidfVectorizer" để chuẩn hóa "genres" với:
        + analyzer='word': chọn đơn vị trích xuất là word
        + ngram_range=(1, 1): mỗi lần trích xuất 1 word
        + min_df=0: tỉ lệ word không đọc được là 0
        Lúc này ma trận trả về với số dòng tương ứng với số lượng film và số cột tương ứng với số từ được tách ra từ "genres"
    """
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0)
    new_tfidf_matrix = tf.fit_transform(movies['genres'])
    return new_tfidf_matrix


def cosine_sim(matrix):
    """
            Dùng hàm "linear_kernel" để tạo thành ma trận hình vuông với số hàng và số cột là số lượng film
             để tính toán điểm tương đồng giữa từng bộ phim với nhau
    """
    new_cosine_sim = linear_kernel(matrix, matrix)
    return new_cosine_sim
