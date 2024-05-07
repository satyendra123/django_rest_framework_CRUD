from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.studentApi),
    path('view/', views.studentApi),
    path('delete/<int:id>/', views.studentApi),
    path('update/<int:id>/', views.studentApi),
    # Add other URL patterns specific to the StudentApp app here
]
