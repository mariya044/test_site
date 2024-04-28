from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer
import logging


logger=logging.getLogger('main')


class UserPagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 2



class UserAPIView(APIView):
    def get(self, request):
        logger.info("info")
        user = User.objects.all().values()
        paginator = UserPagination()
        results = paginator.paginate_queryset(user, request)
        return paginator.get_paginated_response({'users': UserSerializer(results, many=True).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = User.objects.create(
            username=request.data["username"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            password=request.data["password"],
            email=request.data["email"],
            phone_number=request.data["phone_number"]
        )
        return Response({'user': serializer.data})


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    logger.info("info")
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class TestLoginView(APIView):
    def get(self,request):
        return Response("hellow")