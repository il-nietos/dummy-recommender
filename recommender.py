import pandas as pd

def recommend_random(movies, k=5):
    """
    Dummy recommender that recommends a list of random movies. Ignores the actual query.
    """
    return movies['movieId'].sample(k).to_list()
