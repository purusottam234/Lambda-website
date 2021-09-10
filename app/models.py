from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.title
    
    

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()


    
    def __str__(self):
        return self.question
     
    