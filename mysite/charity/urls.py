from django.urls import path



from .views import *
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.conf.urls import url
from django.urls import reverse


urlpatterns = [
    # ex: /polls/
    path('', TemplateView.as_view(template_name="landing_page.html")),
    #path(r'user_verification/', UserVerificationView.as_view()), #need to rewrite the verification class -- the redirect to view -- or has login view
    path('personal-page/', PersonalView.as_view(), name='api_token_auth'),  # <-- get token

    path('register/', CreateUserView.as_view(), name='register'),
    #path(r'personal/', views.personal),
    path('update_hours/', views.update_hours, name='update_hours'),
    path('delete_journal/<id>/', views.delete_journal, name='delete_journal')



]
