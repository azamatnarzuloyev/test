from django.urls import path
from .views import group_views, get_membership, Post_views


urlpatterns = [
    path('myapp/', group_views, name="group-views"),
    path('mem/', get_membership, name='member'),
    path('post/', Post_views, name="post"),
]
