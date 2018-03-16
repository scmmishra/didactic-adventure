from django.urls import include, path

from .views import show, submit, classes

urlpatterns = [
    path('show/', show),
    path('submit/', submit),
    path('campaigns/', classes, {"class": "Campaign"}),
    path('children/', classes, {"class": "Child"}),
    path('courses/', classes, {"class": "Course"}),
    path('mothers/', classes, {"class": "Mother"}),
    path('organizations/', classes, {"class": "Organization"}),
    path('vaccines', classes, {"class": "Vaccine"}),
    path('immunizations/', classes, {"class": "Immunization"}),
]
