from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
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
