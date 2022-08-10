from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='products')
    photo = models.ImageField()





class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=1)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text

