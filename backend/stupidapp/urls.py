from django.urls import include, path

from .views import classes, filter_classes

urlpatterns = [
    path('campaigns/', classes, {"class": "Campaign"}),
    path('children/', classes, {"class": "Child"}),
    path('children/filter/', filter_classes, {"class": "Child"}),
    path('courses/', classes, {"class": "Course"}),
    path('mothers/', classes, {"class": "Mother"}),
    path('mothers/filter/', filter_classes, {"class": "Mother"}),
    path('organizations/', classes, {"class": "Organization"}),
    path('vaccines', classes, {"class": "Vaccine"}),
    path('immunizations/', classes, {"class": "Immunization"}),
]
