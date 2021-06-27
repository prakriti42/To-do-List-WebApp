#This is a py file created to map the content of the app to the project 

from django.urls import path 

from . import views 

from . views import TaskList, TaskDetail , TaskCreate , TaskUpdate , TaskDelete , CustomLoginView , RegisterPage 

from django.contrib.auth.views import LogoutView


#Here I have inserted the urls to display from the views.py 
urlpatterns = [
    path('login/' , CustomLoginView.as_view(), name = "login"),
    path('logout/' , LogoutView.as_view(next_page = 'login'), name = "logout"),
    path('register/' , RegisterPage.as_view() , name = 'register'),
    path('' , TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/' , TaskDetail.as_view(), name = 'task'),
    path('task-create/' , TaskCreate.as_view(), name = 'task-create'),
    path('task-edit/<int:pk>/' , TaskUpdate.as_view(), name = 'task-edit'),
    path('task-delete/<int:pk>/' , TaskDelete.as_view(), name = 'task-delete'),

]

