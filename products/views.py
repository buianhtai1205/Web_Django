from django.shortcuts import render
from django.contrib import admin

from products.models import Product 
from manufacturers.models import Manufacturer 
from django.http import HttpResponse
from collections import OrderedDict

from .fusioncharts import FusionCharts

products = Product.objects.all()
manufacturers = Manufacturer.objects.all()

def myFirstChart(request):
# Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  dataSource = OrderedDict()

# The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  chartConfig["caption"] = "Chart Ecommerce"
  chartConfig["subCaption"] = ""
  chartConfig["xAxisName"] = "Name"
  chartConfig["yAxisName"] = "Price"
  chartConfig["numberSuffix"] = "K"
  chartConfig["theme"] = "fusion"

  dataSource["chart"] = chartConfig
  dataSource["data"] = []

 # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
# Insert the data into the `dataSource['data']` list.
  for manufacturer in manufacturers:
     dataSource["data"].append({"label": manufacturer.name})  

  for product in products:
     dataSource["data"].append({"value": product.price})
 
# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
  column2D = FusionCharts("column2D", "myFirstChart", "800", "600", "myFirstchart-container", "json", dataSource)
  return render(request, 'index.html', {
    'output': column2D.render()
})

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
