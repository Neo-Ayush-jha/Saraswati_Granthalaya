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
    status=models.BooleanField(default=0,blank=True,null=True,choices=((1, 'Available'), (0, 'Unavailable')))
    def __str__(self):
        return self.title
    def descount_price(self):
        result=((self.price-self.discount_price))
        return f"%.2f"% result
    def savePrice(self):
        result=((self.price-self.discount_price)/self.price)*100
        return f"%.2f"% result