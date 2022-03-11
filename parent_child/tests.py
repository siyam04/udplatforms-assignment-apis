from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# App models
from .models import Parent, Child


# Test cases for Parent APIs
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
        response = self.client.post('/api/parents/', data)
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
        data = {
            "first_name": "Edited",
            "last_name": "Parent",
            "street": "Edited",
            "city": "Edited",
            "state": "Edited",
            "zip": "Edited",
        }
        response = self.client.put(reverse('parents-test-detail', args=(self.parent.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete (DELETE): {host}/api/parents/{id}/
    def test_parent_delete(self):
        response = self.client.delete(reverse('parents-test-detail', args=(self.parent.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test cases for Child APIs
class ChildTestCase(APITestCase):

    # Initializing objects
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Parent-002",
            last_name="Testing",
            street="241 Lodge Harper",
            city="Patric Lake",
            state="NYC",
            zip="54456"
        )

        self.child = Child.objects.create(
            first_name="Child-001",
            last_name="Testing",
            parent=self.parent
        )

    # Create (POST): {host}/api/children/
    def test_child_create(self):
        data = {
            "first_name": self.child.first_name,
            "last_name": self.child.last_name,
            "parent": self.parent.id
        }
        response = self.client.post('/api/children/', data)
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
        data = {
            "first_name": "Child-002",
            "last_name": "Edited",
            "parent": self.parent.id
        }
        response = self.client.put(reverse('children-test-detail', args=(self.parent.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete (DELETE): {host}/api/children/{id}/
    def test_child_delete(self):
        response = self.client.delete(reverse('children-test-detail', args=(self.parent.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
