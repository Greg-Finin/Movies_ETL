import pandas as pd

kaggle_metadata = pd.read_csv('/Users/gregfinin/Class/Movies-ETL/movies_metadata.csv')
ratings = pd.read_csv('/Users/gregfinin/Class/Movies-ETL/ratings.csv')
    # Open and read the Wikipedia data JSON file.
with open('/Users/gregfinin/Class//wikipedia-movies.json', mode='r') as file:
    wiki_movies_raw = json.load(file)
    
    # 3. Write a list comprehension to filter out TV shows.
wiki_movies_2 = [movie for movies in wiki_movies_raw
    if ('Director' in movie or 'Directed by' in movie)
        and 'imdb_link' in movie
        and 'No. of episodes' not in movie]

    # 4. Write a list comprehension to iterate through the cleaned wiki movies list
    # and call the clean_movie function on each movie.
clean_wiki_movie = [clean_movie() for movies in wiki_movies_2]

    # 5. Read in the cleaned movies list from Step 4 as a DataFrame.
clean_wiki_movie_df = pd.DataFrame[clean_wiki_movie]
