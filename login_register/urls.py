from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.login,name='login'),
    path('home', views.home,name='home'),
    path('signup', views.signup,name='signup'),
    path('update/<int:id>/', views.update_data,name='update'),
    path('delete/<int:id>/', views.delete_data,name='delete'),
]