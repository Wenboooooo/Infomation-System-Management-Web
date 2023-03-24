from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm



def user_list(request):
    queryset = models.UserInfo.objects.all()


    page_object = Pagination(request, queryset, page_size=10)
    context = {"queryset": page_object.page_queryset,
               "page_string": page_object.html(),}

    return render(request, "user_list.html", context)





def user_add(request):
    """
    Add Users Based On ModelForm
    Advantages of ModelForm:
    1. Help check data submitted by users automatically
    2. Indicate error when input is not correct
    3. Help present variables in html forms automatically
    4. More and more...
    """
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_add.html", {"form": form})
    # Process data when users submit data using post method
    # Check the info valid or not
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    # If any info is invalid
    else:
        return render(request, "user_add.html", {"form": form})


def user_edit(request, nid):
    # Retreat the info from the database according to the nid.
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # Save all info input by users by default
        # form.instance.variable_name = value Use this to create something more than users input
        form.save()
        return redirect("/user/list/")
    # If any info is invalid
    else:
        return render(request, "user_edit.html", {"form": form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")
