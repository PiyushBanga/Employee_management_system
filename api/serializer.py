from .models import Employee , Projects, Skills, EmployeeProjects, EmployeeSkills
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class  SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class EmployeeProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProjects
        fields = '__all__'


class EmployeeSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSkills
        fields = '__all__'        








                     
