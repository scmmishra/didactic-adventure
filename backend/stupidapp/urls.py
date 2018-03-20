from django.urls import include, path, re_path

from .views import classes, filter_classes, ids

urlpatterns = [
    re_path(r'^campaigns/$', classes, {"class": "Campaign"}),
    re_path(r'^campaigns/(?P<id>[0-9]+)/$', ids, {"class": "Campaign"}),
    re_path(r'^children/$', classes, {"class": "Child"}),
    re_path(r'^children/(?P<id>[0-9]+)/$', ids, {"class": "Child"}),
    re_path(r'^children/filter/$', filter_classes, {"class": "Child"}),
    re_path(r'^courses/$', classes, {"class": "Course"}),
    re_path(r'^courses/(?P<id>[0-9]+)/$', ids, {"class": "Course"}),
    re_path(r'^mothers/$', classes, {"class": "Mother"}),
    re_path(r'^mothers/(?P<id>[0-9]+)/$', ids, {"class": "Mother"}),
    re_path(r'^mothers/filter/$', filter_classes, {"class": "Mother"}),
    re_path(r'^organizations/$', classes, {"class": "Organization"}),
    re_path(r'^organizations/(?P<id>[0-9]+)/$', ids, {"class": "Organization"}),
    re_path(r'^vaccines/$', classes, {"class": "Vaccine"}),
    re_path(r'^vaccines/(?P<id>[0-9]+)/$', ids, {"class": "Vaccine"}),
    re_path(r'^immunizations/$', classes, {"class": "Immunization"}),
    re_path(r'^immunizations/(?P<id>[0-9]+)/$', ids, {"class": "Immunization"}),
]
