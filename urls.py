from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    path('insert/', views.studentApi),
    path('view/', views.studentApi),
    path('delete/<int:id>/', views.studentApi),
    path('admin/', admin.site.urls),
]
