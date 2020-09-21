from django.urls import path 
from .views import HomeView , PostDetales

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', PostDetales.as_view(), name='details'),
]
