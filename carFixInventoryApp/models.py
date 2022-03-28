
from django.db import models

# Create your models here.

carmakes=[('toyota','toyota'),('vits','vits'),('tsunami','tsunami'),('isuzu','isuzu'),('Nissan','Nissan')]

class ShopInventory(models.Model):
    '''
    shop inventory model
    '''
    name_of_part=models.CharField(max_length=100,blank=False,default='mcarFix')
    price_of_part= models.DecimalField(max_digits=10, decimal_places=2)
    car_make=models.CharField(choices=carmakes,default='toyota',max_length=50)

    car_model=models.CharField(max_length=100)

class Mechanic(models.Model):
    mechanic_name = models.CharField(max_length=100)
    garage_name = models.CharField(max_length=100)

class Service(models.Model):
    '''
    services  model with mechanic and title unique
    '''
    mechanic = models.ForeignKey(Mechanic, related_name='services', on_delete=models.CASCADE)
    complexity = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['mechanic', 'title']
        ordering = ['complexity']

    def __str__(self):
        return '%d: %s' % (self.complexity, self.title)