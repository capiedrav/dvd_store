from django.db import models


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'language'

    def __str__(self):
        return self.name


class Film(models.Model):
    film_id = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    language = models.ForeignKey(Language, related_name="films_available_in_this_language", on_delete=models.RESTRICT)
    original_language = models.ForeignKey(Language, related_name="films_originally_in_this_language",
                                          on_delete=models.RESTRICT, blank=True, null=True)
    rental_duration = models.PositiveIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.PositiveSmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=5, blank=True, null=True)
    special_features = models.CharField(max_length=54, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film'

    def __str__(self):
        return self.title


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class FilmText(models.Model):
    film_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'film_text'
        verbose_name_plural = "Film Texts"

    def __str__(self):
        return self.title


class FilmCategory(models.Model):
    film = models.OneToOneField(Film, on_delete=models.RESTRICT, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_category'
        unique_together = (('film', 'category'),)
        verbose_name_plural = "Film Categories"

    def __str__(self):
        return self.film.title + " (" + self.category.name + ")"


class Actor(models.Model):
    actor_id = models.SmallAutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'actor'

    def __str__(self):
        return self.first_name + " " + self.last_name


class FilmActor(models.Model):
    actor = models.OneToOneField(Actor, on_delete=models.RESTRICT, primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)
        verbose_name_plural = "Film Actors"

    def __str__(self):
        return self.film.title
