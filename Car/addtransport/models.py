from django.db import models

# Create your models here.

class Transport(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to ='media/images')
    price_tag = models.CharField(max_length = 100)
    post_date = models.DateTimeField(auto_now_add = True )


    def __str__(self):
        return self.name
