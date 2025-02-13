# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Employees(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class EmployeesCopy(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees_copy'


class Salaries(models.Model):
    employee = models.OneToOneField(Employees, models.DO_NOTHING, blank=True, null=True)
    salary = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salaries'
