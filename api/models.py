

# Create your models here.
from django.db import models


# Create Employee model




class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    EmployeeEmail = models.CharField(max_length=50)
    EmployeePhone = models.CharField(max_length=50)
    DateOfBirth = models.DateField(default='2000-01-01')
    Designation = models.CharField(max_length=50)
    DateOfJoining = models.DateField(default='2000-01-01')
    Salary = models.IntegerField(default=0)
    CreatedAt = models.DateTimeField(auto_now_add=True, null=True)
    CreatedBy = models.CharField(max_length=50, default='Admin')
    UpdatedAt = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.CharField(max_length=50, default='Admin')
    IsEmployee = models.BooleanField(default=True)





    def __str__(self):
        return self.EmployeeName 


class Projects(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=50)
    ProjectDescription = models.CharField(max_length=50)
    ProjectManager = models.CharField(max_length=50)
    ProjectStartDate = models.DateField(default='2000-01-01')
    ProjectEndDate = models.DateField(default='2000-01-01')
    CreatedAt = models.DateTimeField(auto_now_add=True, null=True)
    CreatedBy = models.CharField(max_length=50, default='Admin')
    UpdatedAt = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.CharField(max_length=50, default='Admin')
    
    

    def __str__(self):
        return self.ProjectName

    

class Skills(models.Model):
    SkillID = models.AutoField(primary_key=True)
    SkillName = models.CharField(max_length=50)
    def __str__(self):
        return self.SkillName

class EmployeeProjects(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Project = models.ManyToManyField(Projects)
    ProjectRole = models.CharField(max_length=50, default='Employee')
    CreatedAt = models.DateTimeField(auto_now_add=True, null=True)
    CreatedBy = models.CharField(max_length=50, default='Admin')
    UpdatedAt = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.CharField(max_length=50, default='Admin')
    

    def __str__(self):
        return self.Employee.EmployeeName  


class EmployeeSkills(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Skill = models.ManyToManyField(Skills)
    SkillLevel = models.IntegerField(default=0)
    CreatedAt = models.DateTimeField(auto_now_add=True, null=True)
    CreatedBy = models.CharField(max_length=50, default='Admin')
    UpdatedAt = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.CharField(max_length=50, default='Admin')


    def __str__(self):
        return self.Employee.EmployeeName


