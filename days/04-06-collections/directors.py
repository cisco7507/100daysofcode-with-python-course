import csv
from collections import defaultdict, namedtuple
import urllib.request

url = '''https://raw.githubusercontent.com/sundeepblue/\
movie_rating_prediction/master/movie_metadata.csv\
'''
MOVIE_DATA = '/tmp/movie_metadata.csv'

transfer = urllib.request.urlretrieve(url, MOVIE_DATA)

NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    buff = defaultdict(list)
    with open(MOVIE_DATA, 'r') as f:
        r = csv.DictReader(f)
        for entry in r:
            buff[entry['director_name']] += [
                Movie(entry['movie_title'].rstrip(), entry['title_year'], entry['imdb_score'])]
    return buff


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''

    buff = defaultdict(list)
    for director, movies in directors.items():
        if len(movies) < 10 or not director:
            continue

        buff[director]=[movies, _calc_mean(movies)]
    return buff

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    score = 0
    for movie in movies:
        score += float(movie.score)
    div = len(movies)
    # return '{:.2f}'.format(round(score/div))
    if score:
        return (round(score / div, 1))


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    #for director, movie in directors:
    #    print(director, )

def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    [ print(s) for s in directors.items()]


class PyJSON(object):
    def __init__(self, d):
        if type(d) is str:
            d = json.loads(d)
        self.from_dict(d)

    def from_dict(self, d):
        self.__dict__ = {}
        for key, value in d.items():
            if type(value) is dict:
                value = PyJSON(value)
            self.__dict__[key] = value

    def to_dict(self):
        d = {}
        for key, value in self.__dict__.items():
            if type(value) is PyJSON:
                value = value.to_dict()
            d[key] = value
        return d

    def __repr__(self):
        return str(self.to_dict())

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]


if __name__ == '__main__':
    main()
