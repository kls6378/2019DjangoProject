from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=30)
    contents = models.CharField(max_length=300)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title +' | '+ self.name
    
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    contents = models.CharField(max_length=300)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.contents