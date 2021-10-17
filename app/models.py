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



class Team(models.Model):
    img = models.ImageField(upload_to='static/team/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Listing(models.Model):
    Category = models.ForeignKey(
        Category, related_name='listing', on_delete=models.CASCADE)
    listing_title = models.CharField(max_length=200, db_index=True)
    # slug = models.SlugField(max_length=200, db_index=True)
    keyword = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    Address = models.CharField(max_length=100)
    email = models.EmailField()
    Phone = models.IntegerField()
    website = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/listing/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.listing_title






    
     
    