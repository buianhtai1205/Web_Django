from django.shortcuts import render
from django.contrib import admin

from .models import *
from django.http import HttpResponse
from collections import OrderedDict

from .fusioncharts import FusionCharts



def myFirstChart(request):
    # Customer
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Final Sale Price by Customer",
        "showValues": "0",
        "theme": "fusion"
        }
    dataSource['data'] = []

    for key in Product.objects.all():
      data = {}
      data['label'] = key.name
      data['value'] = key.price
      dataSource['data'].append(data)

    plantdataSource = {}
    plantdataSource['chart'] = {
        "caption": "Final Sale Price by Plant",
        "showValues": "0",
        "theme": "fusion"
    }
    plantdataSource['data'] = []

    for key in Manufacturer.objects.all():
      data = {}
      data['label'] = key.name
      data['value'] = key.phone
      plantdataSource['data'].append(data)

    colchart = FusionCharts("column2D", "ex1", "2000", "400", "chart-1", "json", dataSource)
    plantchart = FusionCharts("pie3D", "ex2" , "100%", "400", "chart-2", "json", plantdataSource)

    return render(request, 'index.html', {'output': colchart.render(), 'output2': plantchart.render()})


# def myFirstChart(request):
#   products = Product.objects.all()
#   manufacturers = Manufacturer.objects.all()
# # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
#   dataSource_product = {}

#   chartConfig_column_chart = {}
#   chartConfig_column_chart["caption"] = "Chart Ecommerce"
#   chartConfig_column_chart["subCaption"] = ""
#   chartConfig_column_chart["xAxisName"] = "Name"
#   chartConfig_column_chart["yAxisName"] = "Price"
#   chartConfig_column_chart["numberSuffix"] = "K"
#   chartConfig_column_chart["theme"] = "fusion"

#   dataSource_product["chart"] = chartConfig_column_chart
#   dataSource_product["data"] = []
#   for manufacturer in manufacturers:
#      dataSource_product["data"].append({"label": manufacturer.name})  
#   for product in products:
#      dataSource_product["data"].append({"value": product.price})  
# #  circle chart
#   dataSource_manufacture= {}
#   chartConfig_circle_chart = {}
#   chartConfig_circle_chart['caption'] = "Recommended Portfolio Split",
#   chartConfig_circle_chart['subCaption'] = "For a net-worth of $1M",
#   chartConfig_circle_chart['showValues'] = "1",
#   chartConfig_circle_chart['showPercentInTooltip'] = "0",
#   chartConfig_circle_chart['numberPrefix'] = "$",
#   chartConfig_circle_chart['enableMultiSlicing'] = "1",
#   chartConfig_circle_chart['theme'] = "fusion",
  
#   dataSource_manufacture["chart"] = chartConfig_circle_chart
#   dataSource_manufacture["data"] = []

#   for manufacturer in manufacturers:
#      dataSource_manufacture["data"].append({"label": manufacturer.name})  
#   for product in products:
#      dataSource_manufacture["data"].append({"value": product.price})  

#   column2D = FusionCharts("column2D", "myFirstChart", "800", "600", "myFirstchart-container", "json", dataSource_product)
#   pie3D = FusionCharts("pie3D", "myFirstChart", "100%", "400", "myFirstchart-container2", "json", dataSource_manufacture)
#   return render(request, 'index.html', {
#     'output': column2D.render(),
#     'output2': pie3D.render(),
# })

# # @admin.login()
# def checkAdmin(request):
#     if request.method == 'GET':
#         login_data = request.POST.dict()
#         username = login_data['username']
#         password = login_data['password']
#         num_rows = admin.ModelAdmin.objects.filter(username=username, password=password).count()
#         if num_rows > 0:
#             return render(request, 'products/index.html', {'title':'index'})
#         else:
#             return render("Không có quyền truy cập")
#     return HttpResponse("Sai method")
