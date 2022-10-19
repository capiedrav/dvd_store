from django.contrib import admin
from .models import Language, Film, Category, FilmText, FilmCategory, Actor, FilmActor


# Register your models here.
admin.site.register(Language)
admin.site.register(Film)
admin.site.register(Category)
admin.site.register(FilmText)
admin.site.register(FilmCategory)
admin.site.register(Actor)
admin.site.register(FilmActor)
