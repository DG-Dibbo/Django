from django.db import models
from author.models import Author
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.name