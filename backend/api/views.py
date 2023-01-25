from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

# Create your views here.

# def api_home(request, *args, **kwargs):
#     body = request.body # byte string of json
#     params = request.GET
#     print(params)
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     data['params'] = dict(params)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#     modelData = Product.objects.all().order_by("?").first() ## gives random product
#     data = {}
#     if modelData:
#         # data['content'] = modelData.content
#         # data['title'] = modelData.title
#         # data['price'] = modelData.price
#         data = model_to_dict(modelData, fields=['content','title','price'])
#     return JsonResponse(data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     Django Request Framework API view
#     """
#     instance = Product.objects.all().order_by("?").first() ## gives random product
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#         print(data)
#     return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    Django Request Framework API view
    """
    ## serializer can valiate data as well
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)