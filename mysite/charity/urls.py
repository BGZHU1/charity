from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')

]
