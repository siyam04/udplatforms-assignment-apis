from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# App models
from .models import Parent, Child


# Dummy data for parent create
parent_create_data = {
    "first_name": "Parent",
    "last_name": "Testing",
    "street": "5241 Harper Lodge",
    "city": "Lake Patric",
    "state": "NY",
    "zip": "57445"
}

# Dummy data for parent update
parent_update_data = {
    "first_name": "Parent Updated",
    "last_name": "Lorem",
    "street": "Lorem",
    "city": "Lorem",
    "state": "Lorem",
    "zip": "Lorem"
}


# Test cases for Parent APIs
class ParentTestCase(APITestCase):

    # Initializing object
    def setUp(self):
        self.parent = Parent.objects.create(**parent_create_data)

    # Create (POST): {host}/api/parents/
    def test_parent_create(self):
        response = self.client.post('/api/parents/', self.parent.__dict__)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # List (GET): {host}/api/parents/
    def test_parent_list(self):
        response = self.client.get('/api/parents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Retrieve (GET): {host}/api/parents/{id}/
    def test_parent_detail(self):
        response = self.client.get('/api/parents/', args=self.parent.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Update (PUT): {host}/api/parents/{id}/
    def test_parent_update(self):
        response = self.client.put(reverse('parents-test-detail', args=(self.parent.id,)), parent_update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete (DELETE): {host}/api/parents/{id}/
    def test_parent_delete(self):
        response = self.client.delete(reverse('parents-test-detail', args=(self.parent.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test cases for Child APIs
class ChildTestCase(APITestCase):

    # Initializing objects
    def setUp(self):
        self.parent = Parent.objects.create(**parent_create_data)
        self.child = Child.objects.create(
            first_name="Child",
            last_name="Testing",
            parent=self.parent
        )

        # dummy data for child create
        self.child_create_data = {
            "first_name": self.child.first_name,
            "last_name": self.child.last_name,
            "parent": self.parent.id
        }

        # dummy data for child update
        self.child_update_data = {
            "first_name": "Child Updated",
            "last_name": "Lorem",
            "parent": self.parent.id
        }

    # Create (POST): {host}/api/children/
    def test_child_create(self):
        response = self.client.post('/api/children/', self.child_create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # List (GET): {host}/api/children/
    def test_child_list(self):
        response = self.client.get('/api/children/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Retrieve (GET): {host}/api/children/{id}/
    def test_child_detail(self):
        response = self.client.get('/api/children/', args=self.parent.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Update (PUT): {host}/api/children/{id}/
    def test_child_update(self):
        response = self.client.put(reverse('children-test-detail', args=(self.parent.id,)), self.child_update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete (DELETE): {host}/api/children/{id}/
    def test_child_delete(self):
        response = self.client.delete(reverse('children-test-detail', args=(self.parent.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

