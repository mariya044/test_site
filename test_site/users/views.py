from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
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
        logger.info("info")
        users= User.objects.all()
        paginator = UserPagination()
        return Response ({"users":users})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        users = User.objects.create(
            username=request.data["username"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            password=request.data["password"],
            email=request.data["email"],
            phone_number=request.data["phone_number"]
        )
        return Response({'users': serializer.data})


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    logger.info("info")
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class SignUp(CreateView):
    form_class=UserCreationForm
    template_name="signup.html"
    success_url = reverse_lazy("login")
