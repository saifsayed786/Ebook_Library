from django.db import models
import django.utils.timezone
from django.dispatch import receiver
from .validators import validate_file_extension
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import mark_safe

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Document(models.Model):
    eBookName = models.CharField(max_length=200, default='', null=False, blank=False)
    thumbnail = models.ImageField(upload_to='documents/%Y/%m/%d',editable=False,null=True,blank=True,max_length=255) 
    category =  models.CharField(max_length=200, default='', null=False, blank=False)
    author = models.CharField(max_length=200, default='', null=False, blank=False)
    year_published = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    subcategory = models.CharField(max_length=200, default='', null=True, blank=True)
    eBookFile = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_file_extension], null=True, blank=True)
    eBookData = models.TextField(default='', null=True, blank=True, editable=False)
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)
    addedBy = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    # slug = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
    	return self.eBookName

    def image_tag(self):
    	if self.thumbnail:
    		return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.thumbnail))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    
    

                 