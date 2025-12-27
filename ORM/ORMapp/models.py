from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.
def validate_name_starts_with_a(value) :
    if not value.startswith('a') :
        raise ValidationError('Value must starts with a ')
class Restaurent(models.Model) :
    class TypeChoice(models.TextChoices) :
        INDIAN='IN' 'Indian'
        CHINES='CH' 'Chines'
        ITALIAN='IT' 'Italian'
        GREEK='GR' 'Greek'
        MEXICAN='MX' 'Mexican'
        FASTFOOD='FD' 'Fastfood'
        OTHER='OT' 'Other'
    name=models.CharField(max_length=100,validators=[validate_name_starts_with_a])
    website=models.URLField()
    date_opened=models.DateField()
    latitude=models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    longitude=models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
    restaurent_type=models.CharField(max_length=10,choices=TypeChoice.choices)
    capacity=models.SmallIntegerField(null=True,blank=True)
    nickname=models.CharField(max_length=200,null=True,blank=True)
    comments=GenericRelation('Comments',related_query_name='restaurent')

    def __str__(self):
        return self.name
    
    class Meta :
        ordering=['name']
        get_latest_by=['date_opened']

class Staff(models.Model) :
    
    name=models.CharField(max_length=100)
    restaurents=models.ManyToManyField(Restaurent,through='StaffRestaurent')

    def  __str__(self):
        return self.name

class StaffRestaurent(models.Model) :
    name=models.ForeignKey(Staff,on_delete=models.CASCADE)
    restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE)
    salary=models.FloatField(null=True)

class Rating(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE,related_name='ratings')
    rating=models.PositiveSmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    comments=GenericRelation('Comments')
    def __str__(self):
        return str(self.rating)
class Sales(models.Model) :
    restaurent=models.ForeignKey(Restaurent,on_delete=models.SET_NULL,null=True,related_name='sales')
    datetime=models.DateTimeField()
    income=models.DecimalField(max_digits=8,decimal_places=2) 
    expenditure=models.DecimalField(max_digits=8,decimal_places=2)  

class Product(models.Model) :
    name=models.CharField(max_length=100)
    number_in_stock=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name

class Order(models.Model) :
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    number_of_items=models.PositiveSmallIntegerField()
    #user

    def __str__(self):
        return f'{self.number_of_items}*{self.product.name}'
    
class Comments(models.Model) :
    text=models.TextField()
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type','object_id')