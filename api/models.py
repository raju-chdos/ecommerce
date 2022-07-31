from django.db import models

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    date_create = models.DateField()

    def __str__(self):
        return self.title

class product(models.Model):
    product_tag = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    date_create = models.DateField()

    def __str__(self):
        return self.product_tag





