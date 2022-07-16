from statistics import mode
from django.db import models

# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class Department(ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)

    class Meta:
        db_table = 'department'
        managed = True


class MaritalStatus(ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)

    class Meta:
        db_table = 'marital_status'
        managed = True


class Zone(ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)

    class Meta:
        db_table = 'Zone'
        managed = True


class State(ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)
    abbreviation = models.CharField(max_length=2, null=False)

    class Meta:
        db_table = 'state'
        managed = True


class Supplier(ModelBase):
    name = models.CharField(max_length=64, null=False)
    legal_document = models.CharField(max_length=20, null=False, unique=True)

    class Meta:
        db_table = 'supplier'
        managed = True


class ProductGroup(ModelBase):
    name = models.CharField(max_length=64, null=False)
    commission_percentage = models.DecimalField(max_digits=6, decimal_places=2)
    gain_percentage = models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        db_table = 'product_group'
        managed = True


