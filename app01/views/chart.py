from django.shortcuts import render
from django.http import JsonResponse



def chart_list(request):
    """Data Statistics Page"""
    return render(request, "chart_list.html")


def chart_bar(request):
    """Create the data for the bar chart"""
    # Extract from the database

    legend = ['sales']

    series_list = [
        {
            'name': 'sales',
            'type': 'bar',
            'data': [5, 20, 18, 10, 10, 20]
        }
    ]

    x_axis = ['Jan', 'Feb', 'Mar', 'Apr']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)



def chart_pie(request):
    """Create the data for the pie chart"""

    db_data_list = [
            {'value': 1048, 'name': 'Engine'},
            {'value': 735, 'name': 'Direct'},
            {'value': 580, 'name': 'Email'},
            {'value': 484, 'name': 'Union Ads'},
            {'value': 300, 'name': 'Video Ads'}]


    result = {
        "status": True,
        'data': db_data_list
    }

    return JsonResponse(result)



def chart_line(request):
    legend = ['sales', 'Shanghai']

    series_list = [
        {
            'name': 'sales',
            'type': 'line',
            'stack': 'Total',
            'data': [5, 20, 18, 10,60,15]
        },
        {
            'name': 'Shanghai',
            'type': 'line',
            'stack': 'Total',
            'data': [5, 20, 18, 10, 60, 15]
        }
    ]

    x_axis = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)



