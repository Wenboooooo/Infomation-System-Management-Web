"""DataWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from app01.views import depart, user, num, admin, account, task, order, chart, upload, city
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # Department Management
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/multi/', depart.depart_multi),
    path('depart/index/', depart.depart_index),

    # User Management
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # Mobile Management
    path('num/list/', num.num_list),
    path('num/add/', num.num_add),
    path('num/<int:nid>/edit/', num.num_edit),
    path('num/<int:nid>/delete/', num.num_delete),

    # Admin Management
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # Login Management
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    # Task Management using Ajax to do web interactions
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    # Order Management
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    # Data Statistics
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    # Upload Files
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modelform/', upload.upload_modelform),

    # City List
    path('city/list/', city.city_list),
    path('city/add/', city.city_add ),

]
