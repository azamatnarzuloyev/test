from django.urls import path
from .views import list_views, home_request , ShopViews, reuqestHome_request


urlpatterns = [
    path('list-view/', list_views , name='list-view'),
    path('list-view/<int:pk>/', list_views , name='list-detail'),
    path('home/', home_request , name='home'),
    path('api-shop/', ShopViews.as_view(), name='shop'),
    path('api-shop/<int:pk>/', ShopViews.as_view(), name='shop'),
    path('api-shop/<int:pk>/shop_id=<int:shop_id>/', ShopViews.as_view(), name='shop'),
    path('home-views/', reuqestHome_request , name='home-views'),

]
