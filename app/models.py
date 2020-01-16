from django.db import models

# Create your models here.

class Movie(models.Model):
	moviename = models.CharField(max_length=256)

	def __str__(self):
		return self.moviename

class Producer(models.Model):
	producername = models.CharField(max_length=256)

	def __str__(self):
		return self.producername

class Produces(models.Model):
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    producerid = models.ForeignKey(Producer, on_delete=models.CASCADE)
    cost = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.id)