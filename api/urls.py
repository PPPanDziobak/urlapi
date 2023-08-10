from django.urls import path
from .views import change_url, revert_url


urlpatterns = [
    path('change/', change_url, name='change-url'),
    path('revert/', revert_url, name='revert-url'),
]
