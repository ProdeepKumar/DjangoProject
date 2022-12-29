from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

myjson=open('D:\djangoProject\stock_market_data.json','r')
jsondata=myjson.read()
obj=json.loads(jsondata)
# print(obj['high'])

def hi(request):
    return render(request,'myFirstApp/hi.html',{'obj':obj})
    # return JsonResponse({'obj':obj})
