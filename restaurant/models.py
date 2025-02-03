from django.db import models

# Create your models here.
class  Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    def __str__(self):
        return self.name
    
class Table(models.Model):
    number = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return str(self.number) + ' - ' + self.restaurant.name
    
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.table) + ' - ' + str(self.order_time)