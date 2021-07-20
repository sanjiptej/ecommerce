from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    #  user= models.ForeignKey(User, on_delete=models.CASCADE)
     category_name= models.CharField(max_length=200,unique=True)
     slug = models.SlugField(max_length=200,unique=True)
     description = models.CharField(max_length=500,blank=True)
     cat_image = models.ImageField(upload_to ='photos/categories',blank=True)
    
     class Meta:

        verbose_name = 'category'
        verbose_name_plural= 'categories' 

     def get_url(self):
        return reverse('product_by_category', args=[self.slug])
          
     def __str__(self):
        return str(self.category_name) 
   