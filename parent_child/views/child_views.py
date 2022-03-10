from rest_framework import status, viewsets
from rest_framework.response import Response

# App related
from parent_child.models import Child
from parent_child.serializers.child_serializers import (
    ChildSerializer,
    ChildListSerializer
)


# Create (POST): {host}/api/children/
# List (GET): {host}/api/children/
# Retrieve (GET): {host}/api/children/{id}/
# Update (PUT): {host}/api/children/{id}/
# Delete (DELETE): {host}/api/children/{id}/
class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildListSerializer

    # create & update method override using custom serializer
    def create(self, request, *args, **kwargs):
        serializer = ChildSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ChildSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)





