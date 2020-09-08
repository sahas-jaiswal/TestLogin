from django.db import models


# Create your models here.

class Products(models.Model):
    CATAGORY= (
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door')
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

