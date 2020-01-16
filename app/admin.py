from django.contrib import admin
from app.models import Movie, Producer, Produces

# Register your models here.

admin.site.register(Movie)
admin.site.register(Producer)
admin.site.register(Produces)