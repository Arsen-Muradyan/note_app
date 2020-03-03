from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('add/', views.add),
  path('create/', views.create),
  path('<int:id>', views.show),
  path("edit/<int:id>", views.edit),
  path("update/<int:id>", views.update),
  path("delete/<int:id>", views.delete)
]