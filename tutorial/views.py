from django.http import HttpResponse
from .models import Shop , ShopName
from .serializers import ShopSerializers, Shopnameserializers
from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse, HttpRequest
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from asyncio.log import logger
from rest_framework.decorators import api_view, APIView

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


@csrf_exempt
def home_request(request):
    if request.method =="POST":
        data = io.BytesIO(request.body)
        print(request.body)
        request_data = JSONParser().parse(data)
      
        serializer = Shopnameserializers(data=request_data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)
    

    if request.method =="GET":
        shop = ShopName.objects.all()
        serializer = Shopnameserializers(shop, many=True)
        json = JSONRenderer().render(serializer.data)
        striem = io.BytesIO(json)
        data  =JSONParser().parse(striem)
        return JsonResponse(data , safe=False)
    


        
class ShopViews(APIView):

    def get(self, request, pk=None, shop_id=None):
        if pk:
            shop= Shop.objects.filter(shop_name=pk)
            serializers = ShopSerializers(shop , many=True)
            json = JSONRenderer().render(serializers.data)
            striem = io.BytesIO(json)
            data  =JSONParser().parse(striem)
            try:
                for i in data:
                    if i['id'] ==shop_id:
                        print(i['id'])
                        b = i['id']
                        print(b)
                        dokon = Shop.objects.get(id=b)
                        serializerD = ShopSerializers(dokon) 
                        print(serializerD.data)
                shopname =  ShopName.objects.get(id=pk)

                serializer = ShopSerializers(shopname)
            except Exception as e:
                logger.error(e)
                return JsonResponse({"error": f"{e}"})

            try:
                all_data = {
                    
                    "shop_name":serializer.data,
                    "shop": serializerD.data,
                    "barcha_dokon": data
                }
            
                return JsonResponse(all_data,  safe=False)
            except Exception as e:
                return JsonResponse({"error": f"{e}"})
        else:
            shop = Shop.objects.all()
            serializer=  ShopSerializers(shop, many=True)
            return JsonResponse(serializer.data , safe=False)
    

    

            

    def post(self, request, format=None):
        if request.data['name'] =='hikvision':
            request.data['name'] = 'shop all'

        serializer = ShopSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            return JsonResponse(serializer.data)

        
    def put(self , request, format=None):
        shopname = ShopName.objects.get(id=request.data['id'])
        serializer = Shopnameserializers(shopname, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)



@csrf_exempt
def reuqestHome_request(request):
    if request.method =="GET":
        shop = Shop.objects.all()
        Serialzier = ShopSerializers(shop, many=True)
        json = JSONRenderer().render(Serialzier.data)
        stream = io.BytesIO(json)
        data  = JSONParser().parse(stream)
        print(data)
     
    
        return JsonResponse(data, safe=False)