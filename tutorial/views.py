from django.http import HttpResponse
from .models import Shop
from .serializers import ShopSerializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from asyncio.log import logger


@csrf_exempt
def list_views(request , pk=None):
    if request.method =="GET":
        try:
            if pk is not None:
        
                shop = Shop.objects.get(id=pk)
                print(shop.name)
                serialier = ShopSerializers(shop, many=False)
            else:
                shop = Shop.objects.all()
                serialier = ShopSerializers(shop, many=True)

            json = JSONRenderer().render(serialier.data)
            striem = io.BytesIO(json)
        
            data  =JSONParser().parse(striem)

            return JsonResponse(data, safe=False)
        except Exception as e:
            logger.error(e)
            return JsonResponse({"error": f"{e}"})
        
    if request.method =='POST':
        try:
            body = request.body
            data = io.BytesIO(body)
            shop_data = JSONParser().parse(data)
            serialier = ShopSerializers(data=shop_data)
            if serialier.is_valid(raise_exception=True):
                serialier.save()
                return JsonResponse(shop_data)
        except Exception as e:
            logger.error(e)
            return JsonResponse({"Qiymatni qaytadan kriting":f"{e}"})
        
    

      


            



        
