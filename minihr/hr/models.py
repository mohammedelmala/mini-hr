from django.db import models

# Create your models here.


class Country(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(
        Country, related_name='locations', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=60, unique=True, db_index=True)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    manager = models.ForeignKey(
        'Employee', on_delete=models.SET_NULL, blank=True, null=True, related_name="manage")

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=60)
    rank = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hiredate = models.DateField(auto_now_add=True)
    department = models.ForeignKey(
        Department, related_name="employees", on_delete=models.RESTRICT)
    job = models.ForeignKey(Job, related_name="employees",
                            on_delete=models.RESTRICT)
    grade = models.ForeignKey(
        Grade, related_name="employees", on_delete=models.RESTRICT)
    manager = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    termn_date = models.DateField(blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()
