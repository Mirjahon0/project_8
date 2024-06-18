from django.db import models


class Chairs(models.Model):
    class Price(models.TextChoices):
        sum = 'UZD', 'Sum'
        dollr = 'USD', '$'
        
    name = models.CharField(max_length=50)
    definition = models.TextField()
    prices = models.FloatField(default=30)
    price = models.CharField(max_length=50, choices=Price.choices, default=Price.sum)
    image = models.ImageField(upload_to='product/chairs/')
    slug = models.SlugField(verbose_name='Slug', max_length=255,default='this is not faound')

    def __str__(self):
        return self.name
    

    
class Speciality(models.Model):
    speciality = models.CharField(max_length=20)
    slug = models.SlugField(verbose_name='Slug', max_length=255,default='this is not faound')
    def __str__(self):
        return self.speciality
    
    
   
class Testominal(models.Model):
    msg = models.TextField()
    full_name = models.CharField(max_length=20)
    speciality = models.ManyToManyField(Speciality)
    slug = models.SlugField(verbose_name='Slug', max_length=255,default='this is not faound')
    image = models.ImageField(upload_to='product/testominal/')
    
    def __str__(self):
        return self.full_name

class Links(models.Model):
    facbook = models.URLField(null=True, blank=False)    
    instagramm = models.URLField(null=True, blank=False)    
    twitter = models.URLField(null=True, blank=False)    
    linkidin = models.URLField(null=True, blank=False)
        
    
class Team(models.Model):
    full_name = models.CharField(max_length=30)
    description = models.TextField()  
    speciality = models.ManyToManyField(Speciality)  
    image = models.ImageField(upload_to='product/team/')
    slug = models.SlugField(verbose_name='Slug', max_length=255,default='this is not faound')   
        
