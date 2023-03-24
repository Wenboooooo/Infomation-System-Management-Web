from django.shortcuts import render, HttpResponse
from app01.utils.bootstrap import BootstrapForm, BootstrapModelForm
import os
from app01 import models
from django.conf import settings


def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')

    file_object = request.FILES.get('avatar')


    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()

    print(file_object)
    print(file_object.name)
    return HttpResponse("ok")


from django import forms
class UpForm(BootstrapForm):
    bootstrap_exclude_fields = ["img"]
    name = forms.CharField(label="name")
    age = forms.IntegerField(label="age")
    img = forms.FileField(label="photo")



def upload_form(request):
    title = "Form Upload"
    if request.method=="GET":
        form = UpForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})

    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        # Get img data and its path, then write the path of the img to the database
        image_object = form.cleaned_data.get("img")



        media_path = os.path.join("media", image_object.name)

        f = open(media_path, mode='wb')
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()

        models.Boss.objects.create(
            name = form.cleaned_data['name'],
            age = form.cleaned_data['age'],
            img = media_path,
        )


        return HttpResponse("...")
    return render(request, 'upload_form.html', {"form": form, "title": title})




class UpModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model = models.City
        fields = '__all__'



def upload_modelform(request):
    """Upload files and data based on modelform"""
    title = 'Upload Files Based On ModelForm'
    if request.method =="GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("ok")
    return render(request, 'upload_form.html', {'form': form, 'title': title})








