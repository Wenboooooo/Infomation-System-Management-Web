from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from app01.utils.bootstrap import BootstrapModelForm
from app01 import models
from django import forms
from app01.utils.pagination import Pagination


class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput
        }






def task_list(request):

    queryset = models.Task.objects.all().order_by('-id')

    page_object = Pagination(request, queryset)

    form = TaskModelForm()
    context = {
        "form":form,
        "queryset":page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, "task_list.html", context)



# Exempt csrf token to test post request from the frontend
@csrf_exempt
def task_ajax(request):
    # print(request.GET)
    # print(request.POST)
    data_dict = {"status": True, "data": [11,22,33,44]}
    json_string = json.dumps(data_dict)
    # return HttpResponse(json_string)
    return HttpResponse(json.dumps(data_dict))
    # return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    # print(request.POST)

    # We can check info sent by user using ModelForm in the backend
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        # return a json file if the request is sent by ajax
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    # If validation failed
    data_dict = {"status": False, 'error':form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))















