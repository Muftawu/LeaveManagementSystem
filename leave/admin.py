from django.contrib import admin
from . models import Leave, Staff

admin.site.site_header = "Leave Management System"
admin.site.site_title = "Welcome to Django Leave Management System"

admin.site.register(Leave)
admin.site.register(Staff)