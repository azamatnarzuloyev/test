from django.urls import path
from .views import snippet_list, snippet_detail
urlpatterns = [
    path('app/', snippet_list, name='snippit-list'),
    path('app/<int:pk>/', snippet_detail, name='snippet-detail'),
]
