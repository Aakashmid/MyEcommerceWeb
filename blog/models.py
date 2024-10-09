from django.db import models

# Create your models here.
class Blog(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField( max_length=50)
    head0=models.CharField( max_length=500)
    chead0=models.CharField( max_length=5000)
    head1=models.CharField( max_length=500)
    chead1=models.CharField( max_length=5000)
    head2=models.CharField( max_length=500)
    chead2=models.CharField( max_length=5000)
    pub_date=models.DateField( auto_now_add=True)
    thumbnail=models.ImageField(upload_to="shop\images",default="")

    def __str__(self) -> str:
        return self.title