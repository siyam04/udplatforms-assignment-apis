from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

# App models
from .models import Parent, Child


# Test cases for Parent model
class ParentTestCase(APITestCase):

    # Initializing object
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Parent-001",
            last_name="Testing",
            street="5241 Harper Lodge",
            city="Lake Patric",
            state="NY",
            zip="57445"
        )

    # Create (POST): {host}/api/parents/
    def test_parent_create(self):
        data = {
            "first_name": self.parent.first_name,
            "last_name": self.parent.last_name,
            "street": self.parent.street,
            "city": self.parent.city,
            "state": self.parent.state,
            "zip": self.parent.zip
        }
        response = self.client.post(reverse('parents-test-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # List (GET): {host}/api/parents/
    def test_parent_list(self):
        response = self.client.get(reverse('parents-test-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Retrieve (GET): {host}/api/parents/{id}/
    def test_parent_detail(self):
        response = self.client.get(reverse('parents-test-detail', args=(self.parent.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test cases for Child model
class ChildTestCase(APITestCase):

    # Initializing object
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Parent-002",
            last_name="Testing",
            street="241 Lodge Harper",
            city="Patric Lake",
            state="NYC",
            zip="54456"
        )

    # Create (POST): {host}/api/children/
    def test_child_create(self):
        data = {
            "first_name": "Child-001",
            "last_name": "Test",
            "parent": self.parent.id
        }
        response = self.client.post(reverse('children-test-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # # Update (PUT): {host}/api/children/{id}/
    # def test_child_update(self):
    #     data = {
    #         "first_name": "Child-002",
    #         "last_name": "Test",
    #         "parent": self.parent.id
    #     }
    #     response = self.client.put(reverse('children-test-detail', args=(self.parent.id,)), data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


