from django.db import models

# Create your models here.
class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(max_length=100, default="some default")

    def __str__(self):
        return self.url

class DateExample(models.Model):
    the_data = models.DateTimeField()

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Framework(models.Model):
    name = models.CharField(max_length=10)
    lanugage = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
        
class Charachter(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)
    
    def __str__(self):
        return self.name
        

    






    