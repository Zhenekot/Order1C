from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.IndexView, name='home'),
    path('add_order/', views.add_order, name='add_order'),

]