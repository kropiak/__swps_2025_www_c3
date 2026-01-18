from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Topic, Post
from .serializers import TopicSerializer, CategoryModelSerializer, PostModelSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics


# # określamy dostępne metody żądania dla tego endpointu
# @api_view(['GET'])
# def topic_list(request):
#     """
#     Lista wszystkich obiektów modelu Person.
#     """
#     if request.method == 'GET':
#         topics = Topic.objects.all()
#         serializer = TopicSerializer(topics, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def topic_detail(request, pk):
#     """
#     :param request: obiekt DRF Request
#     :param pk: id obiektu Topic
#     :return: Response (with status and/or object/s data)
#     """
#     try:
#         topic = Topic.objects.get(pk=pk)
#     except Topic.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     """
#     Zwraca pojedynczy obiekt typu Topic.
#     """
#     if request.method == 'GET':
#         topic = Topic.objects.get(pk=pk)
#         serializer = TopicSerializer(topic)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TopicSerializer(topic, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         topic.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['POST'])
# def topic_create(request):
#     serializer = TopicSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def topic_search_by_name(request, phrase):
#     topics = Topic.objects.filter(name__icontains=phrase)
#     serializer = TopicSerializer(topics, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def topic_and_category_search_by_name(request, phrase):
#     topics = Topic.objects.filter(name__icontains=phrase)
#     categories = Category.objects.filter(name__icontains=phrase)
#     topic_serializer = TopicSerializer(topics, many=True)
#     category_serializer = CategoryModelSerializer(categories, many=True)
#
#     my_data = {}
#     my_data['topics'] = topic_serializer.data
#     my_data['categories'] = category_serializer.data
#
#     return Response(my_data)
#
#
# @api_view(['GET'])
# def category_list(request):
#     """
#     Lista wszystkich obiektów modelu Category.
#     """
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategoryModelSerializer(categories, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk):
#     """
#     :param request: obiekt DRF Request
#     :param pk: id obiektu Category
#     :return: Response (with status and/or object/s data)
#     """
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     """
#     Zwraca pojedynczy obiekt typu Category.
#     """
#     if request.method == 'GET':
#         category = Category.objects.get(pk=pk)
#         serializer = CategoryModelSerializer(category)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CategoryModelSerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#

class TopicList(APIView):

    def get(self, request, format=None):
        topic = Topic.objects.all()
        serializer = TopicSerializer(topic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer