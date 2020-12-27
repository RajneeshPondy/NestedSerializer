from django.db import models

class Author(models.Model):
    """Model definition for Author."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + "  " + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    ratings = models.CharField(max_length=2)
    author = models.ForeignKey(Author,
                                related_name='books',
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title