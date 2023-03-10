from rest_framework import generics, authentication, permissions

from .models import Product
from .serializers import ProductSerializer
from api.permissions import IsStaffEditorPermission

from api.authentication import TokenAuthentication

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

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
class ProductCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]


    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(user = self.request.user, content = content)

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     request = self.request
    #     return qs.filter(user = request.user)
        



class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDeleteAPIView(UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# class ProductListAPIView(generics.ListAPIView):

#     """ instead of this method we can use create list view which does both list and creation"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [IsStaffEditorPermission]