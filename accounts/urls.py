from django.urls import path
from . import views
urlpatterns = [
  path('login', views.login),
  path('register', views.register),
  path('signup', views.register_action),
  path('signin', views.login_action),
  path('logout', views.logout_action),
  path('', views.index)
]   