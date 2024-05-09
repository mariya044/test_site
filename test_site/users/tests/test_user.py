from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse


class UserTest(APITestCase):
    def setUp(self):
        self.one_user = User.objects.create(
            email="users@gmail.com",
            phone_number="+37525520948",
            first_name="first",
            last_name="last",
            username="user12",
            password="12345678m"
        )

    def test_user_list(self):
        response = self.client.get(reverse("users"))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data["users"]), 1)


    def test_user_detail(self):
        response = self.client.get(reverse("users_detail", kwargs={"id": self.one_user.id}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_fail_user_detail(self):
        response = self.client.get(reverse("users_detail", kwargs={"id": 12}))
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)