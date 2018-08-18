from django.urls import path

from . import views

app_name = 'Landing'
urlpatterns = [
    path('', views.landing_view, name='home'),
]
