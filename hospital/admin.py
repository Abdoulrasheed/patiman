from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ['idnumber', 'firstname', 'lastname', 'othername', 'department', 'level']


admin.site.register(Student, StudentAdmin)