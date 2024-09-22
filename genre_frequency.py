import pandas as pd
import requests
from tqdm import tqdm
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get sensitive data from environment variables
api_key = os.getenv('OMDB_API_KEY')

# Load the Netflix viewing history CSV (modify the file path accordingly)
file_path = './NetflixDownloads/NetflixViewingHistory.csv'
df_viewing_history = pd.read_csv(file_path)


# A function to search the genre of a movie or series from an API or database
def get_genre_from_title(title):
    """
    This function attempts to get the genre of the title from an online API.
    For simplicity, I'm using the OMDB API, but you can replace it with other sources.
    """
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'Genre' in data:
            return data['Genre']
    return 'Unknown'


# Use tqdm to show progress bar
tqdm.pandas()  # Initialize tqdm

# Add a new column 'Genre' to the dataframe by getting genre for each title
df_viewing_history['Genre'] = df_viewing_history['Title'].progress_apply(get_genre_from_title)

# Count the frequency of each genre
genre_count = df_viewing_history['Genre'].value_counts()

# Save the frequency count to a CSV file
output_path = 'genre_frequency.csv'
genre_count.to_csv(output_path, header=['Frequency'])

print(f"Genre frequency has been saved to {output_path}")
