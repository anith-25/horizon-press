from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Sentence(models.Model):
    sentence = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    