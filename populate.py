import sys, os, django

sys.path.append('..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

django.setup()

from app.models import Movie, Producer, Produces


def populate():

    #Dictionaries with data to add to each Movie, Producer, Produces

    Movies = [
    	{'id' : 1001,
         'moviename': 'movie_a'},
    	{'id' : 1002,
        'moviename': 'movie_b'},
    	{'id' : 1003,
        'moviename': 'movie_c'},
    ]

    Producer = [
    	{'id' : 1001,
        'producername': 'producer_a'},
    	{'id' : 1002,
        'producername': 'producer_b'},
        {'id' : 1003,
        'producername': 'producer_c'},
        {'id' : 1004,
        'producername': 'producer_d'},
    ]

    Produces = [
        {'id'  : 1001,
    	 'movieid': 1001,
         'producerid': 1001,
         'cost': 100,},
        {'id'  : 1002,
    	 'movieid': 1002,
         'producerid': 1002,
         'cost': 200,},
        {'id'  : 1003,
    	 'movieid': 1002,
         'producerid': 1003,
         'cost': 100,},
        {'id'  : 1004,
    	 'movieid': 1001,
         'producerid': 1003,
         'cost': 150,},
    ]

    for i in Movies:
    	movie = add_movie(i['id'] ,i['moviename'])


    for i in Producer:
    	producer = add_producer(i['id'], i['producername'])

    for i in Produces:
        prod = add_produces(i['id'],i['movieid'],i['producerid'],i['cost'])

def add_movie(id, name):
    m = Movie.objects.get_or_create(id=id, moviename=name)[0] #Mind the 0!
    m.save

    return m

def add_producer(id, name):
    p = Producer.objects.get_or_create(id=id, producername=name)[0] #Mind the 0!
    p.save

    return p

def add_produces(id, movieid, producerid, cost):

    movie    = Movie.objects.get(id=movieid)
    producer = Producer.objects.get(id=producerid)

    produces = Produces.objects.get_or_create(id=id,
                                              movieid=movie,
                                              producerid=producer,
                                              cost=cost)[0] #Mind the 0!
    produces.save

    return produces

if __name__ == '__main__':

    print("Populating up!")
    populate()
