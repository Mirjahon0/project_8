from django.urls import path
from .views import ShopListView,AboutListView,ServicesListView, ChairdetailView,ChairUpdateView,ChairDeleteView


urlpatterns = [
    path("shop/", ShopListView.as_view(), name='shops'),
    path("about/", AboutListView.as_view(), name='about'),
    path("service/", ServicesListView.as_view(), name='service'),
    path("shop/<int:id>/", ChairdetailView.as_view(), name='shop-detail'),
    path("update/<int:id>/", ChairUpdateView.as_view(), name='shop-update'),
    path("delete/<int:id>/", ChairDeleteView.as_view(), name='shop-delete'),
    
    
]

