from imdb import IMDb


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, trailer_youtube_url):
        """
        Inits MovieClass with title and trailer_youtube_url.
        """
        # This class uses the library IMDb for retrieving the data
        # of the IMDb movie database about movies.
        # The search is based on movie name and after that by movieID to get
        # the properly movie information sets like title, image and so on.
        imdb = IMDb()
        print("Recovering Movie Data {}".format(movie_title))
        movies = imdb.search_movie(movie_title)
        movie = imdb.get_movie(movies[0].movieID)

        self.title = movie.get('title')
        self.poster_image_url = movie.get('full-size cover url')
        self.rating = movie.get('rating')
        self.director = movie.get('director')[0]
        self.storyline = movie.get('plot')[0]
        self.trailer_youtube_url = trailer_youtube_url
