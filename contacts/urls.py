from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ContactList.as_view(), name='contact-list'),
    path('detail/<str:pk>/', ContactDetail.as_view(), name='contact-detail'),
    
]
