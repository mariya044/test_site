from urllib import request
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer
import logging
from django.core.mail import send_mail


logger=logging.getLogger('main')


class UserPagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 2


class UserAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name="UserView.html"

    def get(self, request):
        logger.info("get")
        serializer = UserSerializer()
        users= User.objects.all()
        paginator = UserPagination()
        results=paginator.paginate_queryset(users,request)
        return Response({'users': users})


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "UserDetails.html"
    logger.info("detail")
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
