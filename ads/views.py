import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Category


def index(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = [{"id": category.id, "name": category.name} for category in categories]
        return JsonResponse(response, safe=False)

    def post(self, request):
        category = Category.objects.create(name=json.loads(request.body)["name"])
        return JsonResponse({"id": category.id, "name": category.name})
