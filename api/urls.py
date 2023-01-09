from django.urls import path
from .views import EmployeeList, EmployeeDetail, ProjectsList, ProjectsDetail, SkillsList, SkillsDetail, EmployeeProjectsList, EmployeeProjectsDetail, EmployeeSkillsList, EmployeeSkillsDetail
from . import views

urlpatterns = [
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
    path('projects/', ProjectsList.as_view()),
    path('projects/<int:pk>/', ProjectsDetail.as_view()),
    path('skills/', SkillsList.as_view()),
    path('skills/<int:pk>/', SkillsDetail.as_view()),
    path('employee_skills/', EmployeeSkillsList.as_view()),
    path('employee_skills/<int:pk>/', EmployeeSkillsDetail.as_view()),
    path('employee_projects/', EmployeeProjectsList.as_view()),
    path('employee_projects/<int:pk>/', EmployeeProjectsDetail.as_view()),

]    