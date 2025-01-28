from django.db import models


class Product(models.Model):
    __tablename__ = 'product'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    price = models.CharField(max_length=10, default='0 RUB')

    def get_dollar_price(self):
        return self.price.replace('RUB', '$')

    def __str__(self):
        return self.name