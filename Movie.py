import fresh_tomatoes

class Movie():

	"""A class used to create movie instances"""

    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_youtube_url

    def show_trailer(self):
        print(self.youtube_url)    

    def print_title(self):
    	print self.title


