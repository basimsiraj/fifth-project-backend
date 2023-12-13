from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    publisher_name = models.CharField(max_length=250)
    featured_image = models.ImageField(upload_to="foods/images")
    ingredients = models.TextField()
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        

