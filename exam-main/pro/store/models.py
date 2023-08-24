from django.db import models
from django.contrib.auth.models import User
from django.db import models




class Product(models.Model)    :
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self) :
        return self.title
    

    def get_display_price(self):
        return self.price 
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def sub_total(self):
        return sum(self.price * self.quantity)


    def get_display_price(self):
        return self.price 
    

    