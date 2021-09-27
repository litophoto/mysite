from django.urls import path

from . import views

app_name = 'polls2'
urlpatterns = [
    path('', views.QuestionList.as_view(), name='question_list'), 
    path('<int:pk>/', views.QuestionDetail.as_view(), name='question_detail'), 
    path('<int:pk>/results/', views.QuestionResults.as_view(), name='question_results'), 
    path('<int:pk>/vote/', views.vote, name='vote'), 
    path('question_create/', views.question_create, name='question_create'), 
]