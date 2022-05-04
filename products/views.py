from django.shortcuts import render

from products.models import Product 
from manufacturers.models import Manufacturer 
from django.http import HttpResponse
from collections import OrderedDict

from .fusioncharts import FusionCharts

products = Product.objects.all()
manufacturers = Manufacturer.objects.all()
# products_list_name = []
# for product in products:
#    products_list_name.append(product.name)

# products_list_price = []
# for product in products:
#    products_list_price.append(product.name)

def myFirstChart(request):
# Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  dataSource = OrderedDict()

# The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
  chartConfig["subCaption"] = "In MMbbl = One Million barrels"
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
  column2D = FusionCharts("column2d", "myFirstChart", "800", "600", "myFirstchart-container", "json", dataSource)
  return render(request, 'index.html', {
    'output': column2D.render()
})

