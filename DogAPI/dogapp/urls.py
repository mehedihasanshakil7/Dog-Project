from django.urls import path
from dogapp import views


urlpatterns = [
    path('', views.DogList.as_view(), name='dog_list'),
    path('<int:pk>/', views.DogDetail.as_view(), name='dog_detail')
]
