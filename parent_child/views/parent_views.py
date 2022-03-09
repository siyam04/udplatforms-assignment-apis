from rest_framework import status, viewsets
from rest_framework.response import Response

# importing app resources
from parent_child.models import Parent
from parent_child.serializers.parent_serializers import ParentListSerializer


# Create (POST): {host}/api/parents/
# List (GET): {host}/api/parents/
# Retrieve (GET): {host}/api/parents/{id}/
# Update (PUT): {host}/api/parents/{id}/
# Delete (DELETE): {host}/api/parents/{id}/
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentListSerializer


