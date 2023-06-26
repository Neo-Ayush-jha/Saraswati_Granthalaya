from django.db import models


class Category(models.Model):
    c_title=models.CharField(max_length=100)
    c_discription=models.CharField(max_length=250)
    def __str__(self):
        return self.c_title
class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
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
    

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=200, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    address = models.CharField(max_length=200, editable=False)
    user_image = models.ImageField()
    DOB = models.DateField()
    Gender = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
    
    def save(self, *args,**kwargs):
        self.full_name = self.first_name + '' + self.last_name
        self.address = self.city + '' + self.state + '' + self.pin_code
        super(User,self).save(*args,**kwargs)
    

    
