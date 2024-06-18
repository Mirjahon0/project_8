from django.urls import path
from .views import BasicViewPage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('' , BasicViewPage.as_view(),name= 'basic'),
]
urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

