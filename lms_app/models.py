from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse

STATUS_CHOICES = ( ('A','A'), ('B','B'), ('C','C')            
                )


class Category(models.Model):
    cat_name = models.CharField("Category Name", max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
    def __unicode__(self):
        return self.cat_name

class Book(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    def __unicode__(self):
       return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    division = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
    def __unicode__(self):
       return self.name