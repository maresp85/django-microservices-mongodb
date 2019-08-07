from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('notes/<int:iduser>', views.NotesView.as_view(), name='notes'),
]
