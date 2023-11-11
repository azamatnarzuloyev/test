from operator import length_hint
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SavdoSerializer, DaysavdoSerializers, Arraydjangoserializer, HistorySerializers
from .models import Savdo, DaySavdoSell, Arraydjango, HistoryField
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView , UpdateAPIView, ListCreateAPIView
from rest_framework import filters



@api_view(["GET", "POST"])
def savdo_views(request):
    if request.method =="GET":
        savdo = Savdo.objects.all()
        serializer = SavdoSerializer(savdo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method =='POST':
        serializer = SavdoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['PUT'])
def savdo_detail(request, pk):
    if request.method =='PUT':
        savdo = Savdo.objects.get(id=pk)
        serializer = SavdoSerializer(savdo , data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['PUT'])
def update_serena(request, pk):
    if request.method =="PUT":
        arraydjango = Arraydjango.objects.get(id=pk)
        c = []
        b = request.data['serena']
        for i  in b:   
            try:   
                arraydjango.serena.remove(i)
            except:
                c.append(i)
                continue
        request.data['serena'] =  arraydjango.serena
        request.data['leng'] = length_hint(arraydjango.serena)
        request.data['error_code'] = c
        serialaser = Arraydjangoserializer(arraydjango, data=request.data)
        if serialaser.is_valid():
           serialaser.save()
           return Response(serialaser.data)
        



class SearchViews(ListAPIView):
    queryset = Arraydjango.objects.all()
    serializer_class = Arraydjangoserializer
  


    

class Createapi(CreateAPIView):
    queryset = Arraydjango.objects.all()
    serializer_class = Arraydjangoserializer


class UpdateApi(UpdateAPIView):
    queryset = Arraydjango.objects.all()
    serializer_class = Arraydjangoserializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    
@api_view(["GET"])
def search_views(request, pk):
    try:
        arraydjango=Arraydjango.objects.get(id=pk)
    except Arraydjango.DoesNotExist:
        return Response({"error":"not fount"})
    
    if request.method =="GET":
       print( length_hint(arraydjango.serena))
       return Response({"error":"not fount"})
    




@api_view(['PUT'])
def updateSerena(request, pk):
    if request.method =="PUT":
        arraydjango = Arraydjango.objects.get(id=pk)
        c = []
        b = request.data['serena']    
        for i  in b:   
            if i in arraydjango.serena:
               c.append(i)
            else:
                arraydjango.serena.append(i)
        request.data['serena'] =  arraydjango.serena
        request.data['error_code'] = c
        serialaser = Arraydjangoserializer(arraydjango, data=request.data)
        if serialaser.is_valid(raise_exception=True):
           serialaser.save()
           return Response(serialaser.data)
        

class HistoryViews(ListCreateAPIView):
    queryset = HistoryField.objects.all()
    serializer_class = HistorySerializers

