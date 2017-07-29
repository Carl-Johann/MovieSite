import Movie
import json
import urllib
import requests
import fresh_tomatoes

# My api key for 'themoviedb' 
api_key = "14c08f8fd0710ca88f23841954112586"

# The url for gettin 'popular' movies
popular_movies_url = "https://api.themoviedb.org/3/movie/now_playing?api_key=" + api_key + "&language=en-US&page=1"
# GET's the JSON 
popular_movies_response = urllib.urlopen(popular_movies_url)
popular_movies_data = json.loads(popular_movies_response.read())

results = popular_movies_data["results"]

# Movie dict to make a html file out of
movies = []
base_image_url = "http://image.tmdb.org/t/p/w342/"
base_youtube_url = "https://www.youtube.com/watch?v="

# Iterates through every movie
for result in results:

    # Gets the some standard attributes
    movie_id = result["id"]
    title = result["title"]
    storyline = result["overview"]
    poster_image_url = base_image_url + result["poster_path"]

    # Makes a GET request for the movie's youtube key. 
    # The key is not included in the GET request for 
    # info about the movie
    base_video_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos"     
    payload = dict(api_key=api_key)
    response = requests.request("GET", base_video_url, data=payload)
    response_text = response.text.decode('utf-8')
    response_text_as_json = json.loads(response_text)
    response_results = response_text_as_json["results"]

    # Some movies don't have a youtube key, so we check if there is one 
    try:
        first_response_result = response_results[0]

        youtube_key = first_response_result["key"]
        youtube_image_url = base_youtube_url + str(youtube_key)        

        movie = Movie.Movie(title, storyline, poster_image_url, youtube_image_url)
        movies.append(movie)

    except IndexError:             
        continue  

# Opens the html file
fresh_tomatoes.open_movies_page(movies)

print("Success")
