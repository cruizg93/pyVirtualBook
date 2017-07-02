from django.db import models


class Location(models.Model):
    zipcode = models.IntegerField(null=True)
    state = models.CharField(max_length=2, null=True)
    county = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    building_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return '{} | {}'.format(self.building_name, self.city)


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    # TODO: billing address

    def __str__(self):
        return '{} | {}'.format(self.name,self.company_name)


class Item(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()
    state = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} | {}'.format(self.description, self.quantity)
