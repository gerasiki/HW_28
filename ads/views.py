import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def index(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = [{"id": category.id, "name": category.name} for category in categories]
        return JsonResponse(response, safe=False)

    def post(self, request):
        category = Category.objects.create(name=json.loads(request.body)["name"])
        return JsonResponse({"id": category.id, "name": category.name})


class CategoryDetailView(View):
    def get(self, request, cat_id):
        if request.method == "GET":
            try:
                category = Category.objects.get(pk=cat_id)
            except Category.DoesNotExist:
                return JsonResponse({'error': 'Not found'}, status=404)

            return JsonResponse({
                "id": category.id,
                "name": category.name
            })


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = [
            {"id": ad.id,
             "name": ad.name,
             "author": ad.author,
             "price": ad.price
             }
            for ad in ads
        ]
        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_request = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_request["name"],
            author=ad_request["author"],
            price=ad_request["price"],
            description=ad_request["description"],
            address=ad_request["address"],
            is_published=ad_request["is_published"]
        )
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }
        )


class AdDetailView(View):

    def get(self, request, ad_id):
        if request.method == "GET":
            try:
                ad = Ad.objects.get(pk=ad_id)
            except Ad.DoesNotExist:
                return JsonResponse({'error': "Not found"}, status=404)

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            }
        )
