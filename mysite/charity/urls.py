from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.landing, name='landing'),
    path('user_login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('personal/<firstname>/', views.personal, name='personal'),
    path('update_hours/', views.update_hours, name='update_hours'),
    path('delete_journal/<id>/', views.delete_journal, name='delete_journal')



]
