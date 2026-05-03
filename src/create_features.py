import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_user_similarity():
    df = pd.read_csv('data/processed/ratings_clean.csv')

    matrix = df.pivot_table(
        index='user_id',
        columns='movie_id',
        values='rating',
        fill_value=0
    )

    similarity = cosine_similarity(matrix)

    joblib.dump(similarity, 'models/user_similarity.pkl')

    logger.info("Feature creation complete!")

if __name__ == "__main__":
    create_user_similarity()
    