from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    category=models.CharField(max_length=150)
    isbn=models.BigIntegerField()
    description=models.TextField()
    price=models.CharField(max_length=150)
    discount_price=models.CharField(max_length=150)
    cover_image=models.ImageField(upload_to="Book-photo/",null=True,blank=True)
    status=models.BooleanField(default=None,blank=True,null=True)