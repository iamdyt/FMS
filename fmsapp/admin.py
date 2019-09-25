from django.contrib import admin
from .models import Staff,Dam,Department,User
# Register your models here.
admin.site.register([Staff,Dam,Department,User])