from django.contrib import admin

from .models import Student, Staff, User
# Register your models here.


admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(User)

