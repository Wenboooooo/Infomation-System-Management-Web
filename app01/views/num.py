from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import MobileModelForm




def num_list(request):
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["mobile__contains"] = search_data




    query_set = models.AccountAdmin.objects.filter(**data_dict).order_by("-level")
    page_object =  Pagination(request, query_set)
    page_queryset = page_object.page_queryset


    page_string = page_object.html()

    context = {
        "search_data": search_data,
        "queryset": page_queryset,
        "page_string": page_string
        }

    """
    <li><a href="/num/list?page=1">1</a></li>
    <li><a href="/num/list?page=2">2</a></li>
    <li><a href="/num/list?page=3">3</a></li>
    <li><a href="/num/list?page=4">4</a></li>
    <li><a href="/num/list?page=5">5</a></li>
    """

    return render(request, "num_list.html", context)




def num_add(request):
    if request.method == "GET":
        form = MobileModelForm()
        return render(request, "num_add.html", {"form": form})

    form = MobileModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/num/list")
    else:
        return render(request, "num_add.html", {"form": form})


def num_edit(request, nid):
    # Retreat the info from the database according to the nid.
    row_object = models.AccountAdmin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = MobileModelForm(instance=row_object)
        return render(request, "num_edit.html", {"form": form})

    form = MobileModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # Save all info input by users by default
        # form.instance.variable_name = value Use this to create something more than users input
        form.save()
        return redirect("/num/list/")
    # If any info is invalid
    else:
        return render(request, "num_edit.html", {"form": form})


def num_delete(request, nid):
    models.AccountAdmin.objects.filter(id=nid).delete()
    return redirect("/num/list")
