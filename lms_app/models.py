from datetime import datetime, timedelta

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

STATUS_CHOICES = ( 
    ('A','A'), 
    ('B','B'), 
    ('C','C')            
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
    is_available = models.BooleanField(default=True)

    def __unicode__(self):
       return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    division = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
    book_number = models.IntegerField(default=0, editable=False)
    block = models.BooleanField(default=False)
   
    def __unicode__(self):
       return self.name + ' - '+ self.dept

class Issue(models.Model):
    student = models.ForeignKey(Student)
    book = models.ForeignKey(Book)
    issue_date = models.DateTimeField("Issue Date", default=datetime.now())
    return_date = models.DateTimeField("Return Date", default=datetime.now()+timedelta(days=7))
    return_status = models.BooleanField(default=True)
    fine_amount = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
       return self.student.name    

    def past_return_date(self):
        return self.return_date < timezone.now() 

    past_return_date.admin_order_field = 'return_date'
    past_return_date.boolean = 'False'
    past_return_date.short_description = 'Past return date?'

