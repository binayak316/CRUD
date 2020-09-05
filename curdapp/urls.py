from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='addpage'),
    path('<id>/delete/', views.delete, name='delete'),
    path('<id>/update/', views.update, name='update'),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout, name='logout'),
]