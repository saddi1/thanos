from . import views
from django.urls import path

from .views import dashboard

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_student, name='create_student'),
    path('<int:pk>/', views.detail_view, name='detail'),

]