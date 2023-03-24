from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination


def admin_list(request):

    # Check whether user has logged in, if not, redirect to the login page
    info = request.session.get("info")
    if not info:
        return redirect('/login/')








    # Search function
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["username__contains"] = search_data

    # Extract data based on search contents
    queryset = models.Admin.objects.filter(**data_dict)


    # Pagination function
    page_object = Pagination(request, queryset)

    context = {"queryset": queryset,
               'page_string': page_object.html(),
               "search_data": search_data
               }
    return render(request, "admin_list.html", context)


from django import forms
from app01.utils.bootstrap import BootstrapModelForm
from django.core.exceptions import ValidationError
from app01.utils.encrypt import md5


class AdminModelForm(BootstrapModelForm):

    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {"password": forms.PasswordInput(render_value=True)}



    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        # Encrypt the password input by administrator
        return md5(pwd)





    def clean_confirm_password(self):
        # print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("Password Does Not Match")
        return confirm



class AdminEditModelForm(BootstrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']




class AdminResetModelForm(BootstrapModelForm):

    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {"password": forms.PasswordInput(render_value=True)}



    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        # Encrypt the password input by administrator
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("Password Cannot Be The Same As The Previous One")

        return md5(pwd)





    def clean_confirm_password(self):
        # print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("Password Does Not Match")
        return confirm






def admin_add(request):
    title = "New Administrator"
    if request.method == "GET":

        form = AdminModelForm()
        return render(request, "change.html", {"form": form, "title": title})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, "change.html", {'form': form, 'title': title})



def admin_edit(request, nid):
    """Edit administrators"""

    # Get none or object
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        msg = "No Administrator Data Found"
        return render(request, "error.html", {"msg": msg})
    title = "Edit Administrator"

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, "change.html", {'form': form, 'title': title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, "change.html", {'form': form, 'title': title})



def admin_delete(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')

def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        msg = "No Administrator Data Found"
        return render(request, "error.html", {"msg": msg})


    title = "Reset Password - {}".format(row_object.username)


    if request.method == "GET":
        form = AdminResetModelForm()

        return render(request, "change.html", {'form': form, 'title': title})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {"form": form, "title": title})




















