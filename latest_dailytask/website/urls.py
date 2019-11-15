from django.contrib import admin
from django.urls import path
from website.views import addTaskUpdate,addProject,addTask,homepage,viewallprojects,projectDetail,dashboard,mytasks,messages,taskDetail,loginpage
urlpatterns = [
    path('addProject/', addProject),
    path('addTask/',addTask),
    path('homepage/',homepage),
    path('viewallprojects/',viewallprojects),
    path('projectDetail/',projectDetail),
    path('dashboard/',dashboard),
    path('mytasks/',mytasks),
    path('messages/',messages),
    path('taskDetail/',taskDetail),
    path('addTaskUpdate/',addTaskUpdate),
    path('loginpage/',loginpage)
]
