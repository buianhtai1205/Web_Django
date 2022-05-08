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
  chartConfig["numberSuffix"] = " VNĐ"
  chartConfig["theme"] = "fusion"

  dataSource["chart"] = chartConfig
  dataSource["data"] = []

 # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
# Insert the data into the `dataSource['data']` list.
  # for manufacturer in manufacturers:
  #    dataSource["data"].append({"label": manufacturer.name})  

  for product in products:
    myLabel = product.name.split(" ")[2] + " " + product.name.split(" ")[3]
    dataSource["data"].append({"label": myLabel})  
    dataSource["data"].append({"value": product.price})
  
  
  dataSource["chart"]["exportEnabled"] = 1
# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
  column2D = FusionCharts("column2D", "myFirstChart", "1500", "600", "myFirstchart-container", "json", dataSource)
  return render(request, 'dartboard1.html', {
    'output1': column2D.render(), 
})

