from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return JsonResponse({"status": "ok"})

