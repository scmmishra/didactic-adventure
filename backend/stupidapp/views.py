from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import Campaign, Child, Course, Immunization, Mother, Organization, Vaccine
import json

# Create your views here.

def show(request):
    return JsonResponse({"message": "Hello, World."})

@csrf_exempt
@require_POST
def submit(request):
    data = json.loads(request.body.decode())
    if "message" in data:
        return JsonResponse({"status": "success", "message": data["message"]})
    return JsonResponse({"staus":"failure", "message": None})

@require_GET
def classes(request, **kwargs):
    klass = {
        "Campaign": Campaign,
        "Child": Child,
        "Course": Course,
        "Immunization": Immunization,
        "Mother": Mother,
        "Organization": Organization,
        "Vaccine": Vaccine
    }
    try:
        response = JsonResponse({"status": "success", "data": list(klass[kwargs["class"]].objects.all())}, status=200)
    except:
        response = JsonResponse({"status": "failure"}, status=404)
    return response
