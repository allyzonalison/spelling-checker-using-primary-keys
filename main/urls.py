from django.urls import path
from main import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('question/<str:pk>/', views.question_page, name='question_page')
]