from django.urls import path

from . import views

app_name = 'piplup'
urlpatterns = [
    path('', views.List.as_view(), name='list'), 
    path('<int:pk>/', views.Detail.as_view(), name='detail'), 
]