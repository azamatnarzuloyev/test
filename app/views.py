from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippitSerializers
from rest_framework import status

@csrf_exempt
def snippet_list(request):
    if request.method  =="GET":
        snippet = Snippet.objects.all()
        serializer = SnippitSerializers(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)
      
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = SnippitSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error_messages, status=400)
    


@csrf_exempt
def snippet_detail(request , pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method =="GET":
        serilizer = SnippitSerializers(snippet)
        return JsonResponse(serilizer.data)

    
    