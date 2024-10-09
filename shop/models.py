from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=400)
    pubdate=models.DateField()
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop\images",default="")
    

    def __str__(self) -> str:
        return self.product_name 
class Contact(models.Model):
 
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=50)
    amount=models.IntegerField(default=0)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=334)
    phone=models.CharField(max_length=12)
    state=models.CharField(max_length=53)
    city=models.CharField(max_length=34)
    zip_code=models.CharField(max_length=12)
    def __str__(self) -> str:
        return self.name
    

    
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField()
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.order_id

