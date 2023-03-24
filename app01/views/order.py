from django.shortcuts import render
from app01 import  models
from app01.utils.bootstrap import BootstrapModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import json
import random
from app01.utils.pagination import Pagination




class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        exclude = ["oid","admin"]



def order_list(request):

    queryset = models.Order.objects.all().order_by("-id")
    page_object = Pagination(request, queryset)
    form = OrderModelForm()

    context = {"form": form, "queryset":page_object.page_queryset, "page_string": page_object.html()}
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """New Order (Ajax request)"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # The data input by users has no oid, so we need to generate an oid manually for each data
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000,9999))
        # Admin variable should also be added
        # form.instance.admin_id = the id of the current admin user
        form.instance.admin_id = request.session["info"]["id"]
        form.save()
        return JsonResponse({"status":True})

    # If failed
    return JsonResponse({"status": False, 'error': form.errors})


def order_delete(request):
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    # print(exists)
    if exists:
        models.Order.objects.filter(id=uid).delete()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": "No data found"})



def order_detail(request):
    """
    First method to present detail of orders

    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "error": "No data found"})

    result = {
        "status": True,
        "data":
            {"title": row_object.title,
             "price": row_object.price,
             "status": row_object.status, }
    }
    return JsonResponse(result)
    """
    uid = request.GET.get("uid")
    row_dict = models.Order.objects.filter(id=uid).values("title","price","status").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "No data found"})
    result = {
        "status": True,
        "data":
            row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """edit"""
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "No data found"})

    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error':form.errors})







