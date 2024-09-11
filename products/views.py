from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer

class ProductListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    serializer_class = ProductSerializer

    def get_queryset(self):
        search = self.request.query_params.get("search")
        if search:
            return Product.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        return Product.objects.all()

    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        image =  request.data.get("image")
        product = Product.objects.create(
            title=title,
            content=content,
            image=image,
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    # def get(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)