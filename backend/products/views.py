from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None

#         if content is None:
#             content = title
#         serializer.save(content = content)


## listcreate does both list and create
class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(content = content)



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(generics.ListAPIView):

    """ instead of this method we can use create list view which does both list and creation"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer