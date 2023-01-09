from django.shortcuts import render, HttpResponse
from .models import Employee, Projects, Skills, EmployeeProjects, EmployeeSkills
from .serializer import EmployeeSerializer, ProjectsSerializer, SkillsSerializer, EmployeeProjectsSerializer, EmployeeSkillsSerializer
from rest_framework import generics

from django.shortcuts import get_object_or_404

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'


class ProjectsList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'


class SkillsList(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    lookup_field = 'pk'

class EmployeeProjectsList(generics.ListCreateAPIView):
    queryset = EmployeeProjects.objects.all()
    serializer_class  = EmployeeProjectsSerializer

   

class EmployeeProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeProjects.objects.all()
    serializer_class = EmployeeProjectsSerializer
    lookup_field = 'pk'


class EmployeeSkillsList(generics.ListCreateAPIView):
    queryset = EmployeeSkills.objects.all()
    serializer_class = EmployeeSkillsSerializer


class EmployeeSkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeSkills.objects.all()
    serializer_class = EmployeeSkillsSerializer
    lookup_field = 'pk'



