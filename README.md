# django_rest_framework_CRUD
i have made a simple crud operation using Django_rest_framework
A) pip install django-cors-headers B) pip install djangorestframework C) 
STEP-1 django-admin startproject SchoolProject
Step-2 CD SchoolProject
Step-3 python manage.py startapp StudentApp
Step-4 ADD all these things in the settings.py Installed Apps 'corsheaders', 'rest_framework', 'StudentApp.apps.StudentappConfig'
Step-5 ADD this line in the settings.py middleware 'corsheaders.middleware.CorsMiddleware'
Step-6 Add the both the lines at the end of the settings.py file CORS_ORIGIN_ALLOW_ALL = True CORS_ALLOW_ALL_HEADERS=True
Step-7 comment out the default database and ADD this database details for using the mysql database DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'sms',
    'USER': 'root',
    'PASSWORD': '',
    }
}
Step-8 models.py file 

from django.db import models
class Student(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    fee = models.IntegerField()

Step-9 make a file named serializers.py 

from rest_framework import serializers
from StudentApp.models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
Step-10 open the mysql database and make a database named called sms which we have defined in the settings.py database details. just make the database only not make the tables inside the database. tables will be generating automatically through the models.py file after running the following command
Step-11 python manage.py makemigrations and after that run the python python manage.py migrate after that go into the xamp database and check table is created or not

Step-12 views.py file
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student

@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        student = Student.objects.all()
        student_serializer=StudentSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(id=id)
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        student=Student.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)

Step-13 this is the main urls.py file. i have not made the persional urls for every project folder so in the main urls file we write this code

from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
path('insert/', views.studentApi),
path('view/', views.studentApi),
path('delete/<int:id>/', views.studentApi),
path('admin/', admin.site.urls),
]

Step-14 after that open the terminal and run the code by writing python manage.py runserver

Step-12 POST COMMAND - now we will open the postman and send the data for testing give this url http://localhost:8000/student/insert/ and the data in the body raw json {
    "name": "John Doe",
    "address": "123 Main St",
    "fee": 5000
} then after clicking on the send then "Added Successfully" message will be printed on the postman. also you can check by going into the database whether the data is inserted or not

Step-13 GET COMMAND http://localhost:8000/student/view/ and you will see the every data fetched from the database and printed on the postman like this 
[
{
"id": 3,
"name": "Satyam",
"address": "noida 61",
"fee": 9000
},
]

Step-14 DELETE COMMAND http://localhost:8000/student/delete/3/ so id 3 will be deleted.
Step-15 PUT COMMAND- i have not used the put command. basically put command is used for update. in this also we need to pass the id in the url
