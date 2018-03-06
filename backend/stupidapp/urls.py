from django.urls import include, path

from .views import show, submit

urlpatterns = [
    path('show/', show),
    path('submit/', submit),
]
