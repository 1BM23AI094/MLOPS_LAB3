import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_ratings(df):
    required = {'user_id', 'movie_id', 'rating', 'timestamp'}
    if not required.issubset(df.columns):
        raise ValueError("Missing columns")

    df = df[(df['rating'] >= 1.0) & (df['rating'] <= 5.0)]
    return df

def process_ratings():
    logger.info("Loading raw data...")
    df = pd.read_csv('data/raw/ratings.csv')

    df = validate_ratings(df)

    df = df.drop_duplicates(subset=['user_id', 'movie_id'])

    Path('data/processed').mkdir(exist_ok=True)

    df.to_csv('data/processed/ratings_clean.csv', index=False)

    logger.info("Processing complete!")

if __name__ == "__main__":
    process_ratings()