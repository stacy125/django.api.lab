from django.db import models

# Create your models here.

class Book(models.Model):
    
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    # String Magic Method
    # Makes debugging easier!

    def __str__(self):
        return self.author
