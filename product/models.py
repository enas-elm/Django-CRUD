from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    stock = models.IntegerField(null=True)
    image = models.ImageField(upload_to='product/static/images/', null=True)

    # défini le nom de l'instance
    def __str__(self):
        return self.name