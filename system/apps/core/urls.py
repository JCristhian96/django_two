from django.urls import path
# Views
from . import views

app_name = 'core'

urlpatterns = [
    path(
        '', views.PersonListView.as_view(), name='list'
    ),
    path(
        'add/', views.PersonCreateView.as_view(), name='add'
    ),
    path(
        'edit/<pk>/', views.PersonUpdateView.as_view(), name='edit'
    ),
    path(
        'delete/<pk>/', views.PersonDeleteView.as_view(), name='delete'
    ),
]
