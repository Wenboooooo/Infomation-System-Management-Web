from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.bootstrap import BootstrapModelForm


def city_list(request):
    queryset = models.City.objects.all()
    return render(request, 'city_list.html', {'queryset': queryset})




class UpModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model = models.City
        fields = '__all__'



def city_add(request):
    title = 'New City'
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/city/list/')
    return render(request, 'upload_form.html', {'form': form, 'title': title})