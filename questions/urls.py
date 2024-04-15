from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),

    path('complete/', views.complete, name='complete'),

    path('exam/', views.exam, name = 'exam'),

    path('grading/', views.grading, name = 'grading'),

    path('user/', views.user, name = 'user'),
]