from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Group, Membership, Person, ModelTest
from .serializers import GroupSerializers, PersonSerializers, MemBerSerializers, ModelTestSeralizers


@api_view(['GET'])
def  group_views(request):
    group = Group.objects.all()
    serializer = GroupSerializers(group, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_membership(request):
    memberships = Membership.objects.all()
    serializers = MemBerSerializers(memberships, many=True)
    return Response(serializers.data)


@api_view(["POST"])
def Post_views(request):
    if request.method =="POST":
        serialiser = ModelTestSeralizers(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
    





