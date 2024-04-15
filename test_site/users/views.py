from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer


class UserAPIView(APIView):
    def get(self, request):
        user=User.objects.all().values()
        return Response({'users':list(user)})
    def post(self,request):
        new_user=User.objects.create(
            email=request.data["email"]
        )
        return Response({'user': model_to_dict(new_user)})

