from itertools import product
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

class Product(ModelBase):
    name = models.CharField(max_length=64, null=False)
    cost_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    sale_price = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    product_group = models.ForeignKey(
        to = 'ProductGroup',
        on_delete = models.DO_NOTHING,
        db_column = 'id_product_group',
        null = False
    )
    supplier = models.ForeignKey(
        to = 'Supplier',
        db_column='id_supplier',
        on_delete=models.DO_NOTHING,
        null = False
    )
    class Meta:
        db_table = 'product'
        managed = True

