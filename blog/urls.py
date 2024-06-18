from django.urls import path
from .views import BlogListView,BlogDetailView,BlogUpdateView,BlogDeleteView
urlpatterns = [
   path('blog/',BlogListView.as_view(),name='blogs'),
   path("blog/<int:id>/", BlogDetailView.as_view(), name='blog-detail'),
   path("update/<int:id>/",BlogUpdateView.as_view(), name='blog-update'),
   path("delete/<int:id>/",BlogDeleteView.as_view(), name='blog-delete'),
    
]
