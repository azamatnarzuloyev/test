from django.urls import path
from .views import savdo_views, savdo_detail, SearchViews, Createapi, UpdateApi, update_serena, search_views, updateSerena

urlpatterns = [
    path('savdo/', savdo_views, name='savdo-get'),
    path('savdo/<int:pk>/', savdo_detail, name='savdo-detail'),
    path('get-serena/', SearchViews.as_view(), name='delete'),
    path('create/', Createapi.as_view(), name='create'),
    path('create/<int:pk>/', UpdateApi.as_view(), name='update'),
    path('serena-update/<int:pk>/', update_serena ,name='update-serena'),
    path('search/<int:pk>/', search_views, name='search'),
    path('update-shop/<int:pk>/', updateSerena , name='update')
]
