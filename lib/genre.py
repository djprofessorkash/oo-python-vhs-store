from .movie_genre import MovieGenre

class Genre:
    all = []
    def __init__( self, name ):
        self.name = name
        Genre.all.append( self )
