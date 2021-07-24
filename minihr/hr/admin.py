from django.contrib import admin
from hr import models

# Register your models here.
admin.site.register(models.Country)
admin.site.register(models.Location)
admin.site.register(models.Department)
admin.site.register(models.Job)
admin.site.register(models.Grade)
admin.site.register(models.Employee)
