from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Media(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    premiere = models.DateField()
    rating = models.IntegerField()
    votes = models.IntegerField()
    external_id = models.CharField(max_length=10)
    genres = models.ManyToManyField(Genre)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    media = models.ManyToManyField(Media)


#class User(models.Model):
#    username = models.CharField(max_length=45)
#    email = models.EmailField()
#    gender = models.CharField(max_length=1)
#    password = models.CharField(max_length=32)
#    birth_date = models.DateField()
#    admin = models.BooleanField()
#    media = models.ManyToManyField(Media)


class Episode(models.Model):
    title = models.CharField(max_length=45)
    airdate = models.DateTimeField()
    description = models.CharField(max_length=255)
    season = models.IntegerField()
    number = models.IntegerField()
    series = models.ForeignKey(Media)

    def __unicode__(self):
        return self.title


class Media_Request(models.Model):
    title = models.CharField(max_length=45)
    external_id = models.CharField(max_length=10)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
