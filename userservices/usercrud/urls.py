from django.urls import path, include
from . import views

urlpatterns = [
     path('userslist/', views.UserList.as_view(), name='userslist'),
     path('users/', views.UsersView.as_view(), name='users'),
     path('users/<int:pk>', views.UsersView.as_view(), name='users'),
     path('usersearch/', views.UsersSearch.as_view(), name='usersearch'),
]
