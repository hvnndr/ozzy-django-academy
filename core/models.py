from itertools import product
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

    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')


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


class City(ModelBase):
    name = models.CharField(max_length=64, null=False)
    state = models.ForeignKey(
        to = 'State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False
    )
    class Meta:
        db_table = 'city'
        managed = True

class District(ModelBase):
    name = models.CharField(max_length=64, null=False)
    city = models.ForeignKey(
        to = 'City',
        db_column='id_city',
        null=False,
        on_delete=models.DO_NOTHING
    )
    zone = models.ForeignKey(
        to = 'Zone',
        db_column='id_zone',
        null=False,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = 'district'
        managed = True


class Employee(ModelBase):
    name = models.CharField(max_length=64, null=False)
    salary = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    gender = models.CharField(max_length=1, null=False, choices=ModelBase.Gender.choices)
    admission_date = models.DateField(null=False)
    birth_date = models.DateField(null=False)
    district = models.ForeignKey(
        to = 'District',
        on_delete=models.DO_NOTHING,
        null = False,
        db_column='id_district'
    )
    department = models.ForeignKey(
        to = 'Department',
        on_delete=models.DO_NOTHING,
        null = False,
        db_column='id_department'
    )
    marital_status = models.ForeignKey(
        to = 'MaritalStatus',
        db_column='id_marital_status',
        on_delete=models.DO_NOTHING,
        null=False
    )

    class Meta:
        db_table = 'employee'
        managed = True


class Branch(ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)
    district = models.ForeignKey(
        to = 'District',
        db_column='id_district',
        on_delete=models.DO_NOTHING,
        null=False
    )

    class Meta:
        db_table = 'branch'
        managed = True


class Customer(ModelBase):
    name = models.CharField(max_length=64, null=False)
    income = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    gender = models.CharField(max_length=1, null=False, choices=ModelBase.Gender.choices)
    district = models.ForeignKey(
        to = 'District',
        db_column='id_district',
        on_delete=models.DO_NOTHING,
        null=False
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )

    class Meta:
        db_table = 'customer'
        managed = True


class Sale(ModelBase):
    date = models.DateTimeField(auto_now_add=True, null=False)
    costumer = models.ForeignKey(
        to = 'Customer',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_customer'
    )
    employee = models.ForeignKey(
        to = 'Employee',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_employee'
    )
    branch = models.ForeignKey(
        to = 'Branch',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_branch'
    )

    class Meta:
        db_table = 'sale'
        managed = True


class SaleItem(ModelBase):
    quantity = models.DecimalField(max_digits=16, decimal_places=3)
    sale = models.ForeignKey(
        to = 'Sale',
        db_column='id_sale',
        on_delete=models.DO_NOTHING,
        null=False
    )
    product = models.ForeignKey(
        to = 'Product',
        db_column='id_product',
        on_delete=models.DO_NOTHING,
        null=False
    )

    class Meta:
        db_table = 'sale_item'
        managed = True