from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name="home"),
  path('join', views.join, name="join"),
  path('edit/<int:pk>', views.edit, name='edit'),
  path('delete/<int:pk>/', views.delete_member, name='delete_member'),
]