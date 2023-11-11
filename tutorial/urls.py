from django.urls import path
from .views import list_views


urlpatterns = [
    path('list-view/', list_views , name='list-view'),
    path('list-view/<int:pk>/', list_views , name='list-detail'),

]
