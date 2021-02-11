from django.contrib import admin
from .models import employee, manager
# Register your models here.
admin.site.register(employee)
admin.site.register(manager)