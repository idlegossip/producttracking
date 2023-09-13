from django.db import models

# Create your models here.

class Company(models.Model):
    companyName= models.CharField(max_length=200, blank=False, null=False)
    place = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.companyName


class Employe(models.Model):
    companyName = models.ForeignKey(Company, on_delete=models.CASCADE)
    employeName = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.employeName
    

class Product(models.Model):
    devicename = models.CharField(max_length=200, blank=False, null=False)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.devicename
    

class UseProduct(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    takenTime = models.DateTimeField(auto_now_add=True)
    takenQuality = models.CharField(max_length=255, blank=False)
    returnTime = models.DateTimeField(auto_now=True)
    returnQuality = models.CharField(max_length=255, blank=True)
    isReturn = models.BooleanField(default=False)
    class Meta:
        unique_together = ('employe', 'product')

    def __str__(self):
        return 'Taken Time: ' + str(self.takenTime) + '    |    ' + 'Return Time: ' + str(self.returnTime)
