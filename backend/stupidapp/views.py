from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.core.serializers import serialize
from .models import Campaign, Child, Course, Immunization, Mother, Organization, Vaccine
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def classes(request, *args, **kwargs):
    if request.method == "GET":
        return get_classes(request, *args, **kwargs)
    else:
        return post_classes(request, *args, **kwargs)
        
klasses = {
    "Campaign": Campaign,
    "Child": Child,
    "Course": Course,
    "Immunization": Immunization,
    "Mother": Mother,
    "Organization": Organization,
    "Vaccine": Vaccine
}

@require_GET
def get_classes(request, *args, **kwargs):
    try:
        klass = klasses[kwargs["class"]]
        response = JsonResponse({"status": "success", "data": json.loads(serialize("json", klass.objects.all()))}, status=200)
    except:
        response = JsonResponse({"status": "failure"}, status=404)
    return response

@require_GET
def ids(request, id, *args, **kwargs):
    try:
        klass = klasses[kwargs["class"]]
        response = JsonResponse({"status": "success", "data": json.loads(serialize("json", [klass.objects.get(id=id)]))[0]}, status=200)
    except:
        response = JsonResponse({"status": "failure"}, status=404)
    return response

@csrf_exempt
@require_POST
def post_classes(request, *args, **kwargs):
    try:
        klass = klasses[kwargs["class"]]
        data = json.loads(request.body)
        entry = klass(**data)
        entry.save()
        response = JsonResponse({"status": "success", "data": json.loads(serialize("json", [klass.objects.get(id=entry.id)]))[0]}, status=200)
    except:
        response = JsonResponse({"status": "failure"}, status=422)
    return response

fields = {
    "Child": {
        "id": "id__contains",
        "first_name": "first_name__contains",
        "last_name": "last_name__contains",
        },
    "Mother": {
        "id": "id__contains",
        "first_name": "first_name__contains",
        "last_name": "last_name__contains",
    }
}

@csrf_exempt
@require_POST
def filter_classes(request, *args, **kwargs):
    try:
        data = json.loads(request.body)
        page, entries = data["page"], data["entries"]
        query_dict = {fields[kwargs["class"]][key]: value for key, value in data["fields"].items()}
        query = klasses[kwargs["class"]].objects.filter()
        for key, value in query_dict.items():
            query = query.filter(**{key: value})
        data_query = query[(page-1)*entries:page*entries]
        count_query = query.count()
        response = JsonResponse({"status": "success", "data": json.loads(serialize("json", data_query)), "count": count_query}, status=200)
    except:
        import traceback
        traceback.print_exc()
        response = JsonResponse({"status": "failure"}, status=422)
    return response
