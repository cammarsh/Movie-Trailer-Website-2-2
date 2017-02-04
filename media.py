import webbrowser

#code defining the classes video, movie, and TvShow, and creating their __init
#functions and class variables to show information about various
#forms of media.

class Video():

    def __init__(self, watch_title, poster_image_url, duration):
        self.title= watch_title
        self.poster_image_url= poster_image_url
        self.duration= duration

class Movie(Video):
    """This class provides a way to store information pertaining to movies."""

    def __init__(self, watch_title, movie_storyline, poster_image_url, duration,
                 trailer_youtube_url, movie_actors):
        Video.__init__(self, watch_title, poster_image_url, duration)
        self.trailer_youtube_url= (trailer_youtube_url)
        self.movie_storyline= movie_storyline
        self.movie_actors= movie_actors

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

#class TvShow(Video):
 #   """This class provides a way to store information about TV shows."""
   # def __init__(self, watch_title, watch_storyline, poster_image_url, duration, seasons,
 #                episodes, tv_station, tvshow_actors):
 #       Video.__init__(self, watch_title, watch_storyline, poster_image_url, duration)
  #      self.season= seasons
  #      self.episodes= episodes
  #      self.station= tv_station_url
  #      self.stars= tvshow_actors

    
    
        
