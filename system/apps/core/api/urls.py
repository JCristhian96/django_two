from django.urls import path
# Views
from . import views

app_name = 'core_api'

urlpatterns = [
    path('persons/', views.PersonAPIView.as_view(), name='list'),    
]
