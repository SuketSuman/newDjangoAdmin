from http import HTTPStatus

from django import views
from django.http import JsonResponse
from django.shortcuts import render

from apps.ecommerce.forms import ProductForm
from apps.ecommerce.models import Products


class ProductsView(views.View):

    def get(self, request):
        form = ProductForm()
        return render(request, "", context={
            "form": form
        })

    def post(self, request):
        product = ProductForm(request.POST)
        if not product.is_valid():
            return JsonResponse(data={
                "detail": ""
            }, status=HTTPStatus.BAD_REQUEST)
        product.save()
        return JsonResponse(data={
            "detail": ""
        }, status=HTTPStatus.OK)

    def put(self, request, product_id):
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return JsonResponse(data={
                "message": ""
            }, status=HTTPStatus.NOT_FOUND)
        product_form = ProductForm(request.PUT, instance=product)
        if not product_form.is_valid():
            return JsonResponse(data={
                "detail": ""
            }, status=HTTPStatus.BAD_REQUEST)
        return JsonResponse(data={
            "detail": ""
        }, status=HTTPStatus.OK)

    def delete(self, request, product_id):
        to_delete_product = Products.objects.filter(id=product_id)
        if to_delete_product.count() == 0:
            return JsonResponse(data={
                "detail": ""
            }, status=HTTPStatus.NOT_FOUND)
        to_delete_product.delete()
        return JsonResponse(data={
            "detail": ""
        }, status=HTTPStatus.OK)
