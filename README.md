# Steps to build the Dog-Project

### Before all, python must be installed in system

## Step-1: Creating virtual environment
Create an empty folder "Dog-Project". Inside the folder create virtual environment<br/>
`python -m venv env`

## Step-2: Activation of virtual envvironment
Activate the virtual environment<br/>
`cd env`<br/>
`cd Scripts`<br/>
`activate`

## Step-3: Django and rest framework installtion
Go back to the project folder "Dog-Project" and install Django and rest framework<br/>
`pip install django`<br/>
`pip install djangorestframework`

## Step-4: Creating Project
Create a new Django project "DogAPI"<br/>
`django-admin startproject DogAPI`

## Step-5: Run Project
Run the project if it is working properly<br/>
`python manage.py runserver`

## Step-5: Creating app
Create a new app "dogapp"<br/>
`python manage.py startapp dogapp`

## Step-6: Including app in project
Go to the settings.py file inside DogAPI and add 'dogapp' and 'rest_framework' in INSTALLED_APPS

## Steps-7: Implemienting the app
Go to the "dogapp" folder.<br/>
Implement Dog model inside models.py<br/>
Create serializers.py and implement serializer including all fields of Dog model.<br/>
In views.py implement CRUD operations for the Dog model<br/>
Create urls.py and define the urls<br/>
Go to the urls.py in "DogAPI" and include urls.py of the "dogapp"

## Steps-8: Documentation
Install the module `pip install drf-yasg`<br/>
Go to settings.py and add this `'drf_yasg',` in INSTALLED_APPS<br/>
Go to urls.py in "DogAPI" and add the code snippet<br/>

```
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
```
```
schema_view = get_schema_view(
   openapi.Info(
      title="Dog API",
      default_version='v1',
      description="Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dogapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
```
```
urlpatterns = [
    path('documentation.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```
For more details click [on me](https://drf-yasg.readthedocs.io/en/stable/readme.html#installationhttps://drf-yasg.readthedocs.io/en/stable/readme.html#installation)

## Step-9: Unit testing
Go to tests.py in "dogapp" and implement the testing<br/>
After implementing tests.py, test the project<br/>
```python manage.py test```
