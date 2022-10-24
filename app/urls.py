from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<url>/', views.redirect_to_orginal_url),
]
