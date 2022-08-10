from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Product
from main.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':

        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data)
