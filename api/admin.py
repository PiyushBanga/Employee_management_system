

# Register your models here.
from django.contrib import admin
from .models import Employee, Projects, Skills, EmployeeProjects , EmployeeSkills
# Register your models here.
admin.site.register(Employee)
admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(EmployeeProjects)
admin.site.register(EmployeeSkills)