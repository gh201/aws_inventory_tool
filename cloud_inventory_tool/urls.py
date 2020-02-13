from django.urls import path, include
from frontend.urls import urlpatterns

urlpatterns = [
    path('', include('frontend.urls')),
]
