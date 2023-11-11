from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from .serializers import ProductSerialasers, Productmaterial
from .models import Product, MeteraialProduct

class ProductViews(ListCreateAPIView):
    
    serializer_class = ProductSerialasers
    lookup_field="pk"

    def get_queryset(self):
        queryset =Product.objects.all()
        prodname = self.request.query_params.get("productName")
        if prodname:
            queryset = queryset.filter(name__isstartswith=prodname)
        return queryset



class ProductmaterialViews(ListCreateAPIView):
    queryset = MeteraialProduct.objects.all()
    serializer_class = Productmaterial
    lookup_field="pk"

    

