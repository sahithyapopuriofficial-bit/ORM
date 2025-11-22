from django.db import models
from django.contrib import admin
class Product(models.Model):
    Name=models.CharField(max_length=100)
    Product_Id=models.IntegerField(primary_key=True)
    Brand=models.CharField(max_length=20)
    Price=models.FloatField()
    Manufacture_date=models.DateField()
    Expiry_date=models.DateField()
    Warranty=models.CharField(max_length=10)
class ProductAdmin(admin.ModelAdmin):
    list_display=['Name','Product_Id','Brand','Price','Manufacture_date','Expiry_date','Warranty']   
    actions_on_bottom=True