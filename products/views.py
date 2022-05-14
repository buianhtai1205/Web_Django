from django.shortcuts import render

from products.models import Product 
from manufacturers.models import Manufacturer 
from django.db.models import Count

from .fusioncharts import FusionCharts


def myFirstChart(request):
  plantdataSource = {}
  plantdataSource['chart'] = {
      "caption": "Product Count Statistics",
      "numberSuffix": " SP",
      "exportEnabled": "1",
      "theme": "fusion"
  }
  plantdataSource['data'] = []
  for item in Manufacturer.objects.raw('SELECT manufacturers_manufacturer.id, manufacturers_manufacturer.name, COUNT(manufacturers_manufacturer.name) AS num_products FROM manufacturers_manufacturer JOIN products_product ON manufacturers_manufacturer.id = products_product.manufacturer_id_id GROUP BY manufacturers_manufacturer.id, manufacturers_manufacturer.name'):
    data = {}
    data['label'] = item.name
    data['value'] = item.num_products
    plantdataSource['data'].append(data)
  plantchart = FusionCharts("pie3D", "myFirstChart" , "1500", "700", "myFirstchart-container", "json", plantdataSource)
  return render(request, 'dartboard1.html', {'output': plantchart.render()})


def mySecondChart(request):
  dataSource = {}
  dataSource['chart'] = {
    "caption": "Product Price Statistics",
    "xAxisName": "Name",
    "yAxisName": "Price",
    "numberSuffix": " VNĐ",
    "exportEnabled": "1", 
    "theme": "fusion",
    }
  dataSource['data'] = []

  id = request.GET.get('id')
  if id == '-1':
    products = Product.objects.all()
  else:
    products = Product.objects.filter(manufacturer_id_id=id)
    dataSource['chart']['theme'] = "umber"

  for product in products:
    myLabel = product.name[11:]
    dataSource["data"].append({"label": myLabel})  
    dataSource["data"].append({"value": product.price})

  if id == '-1':
    column2D = FusionCharts("column2D", "mySecondChart", "1400", "700", "myFirstchart-container", "json", dataSource)
  else:
    column2D = FusionCharts("column2D", "mySecondChart", "1200", "700", "myFirstchart-container", "json", dataSource)
  return render(request, 'dartboard2.html', { 'output': column2D.render(), })

