from rest_framework import serializers

# App related
from parent_child.models import Parent, Child
from .parent_serializers import ParentListSerializer


# Child Create & Update Serializer
class ChildSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(many=False, queryset=Parent.objects.all())

    class Meta:
        model = Child
        fields = ('id', 'first_name', 'last_name', 'parent')


# Child List Serializer
class ChildListSerializer(serializers.ModelSerializer):
    parent = ParentListSerializer(read_only=True)

    class Meta:
        model = Child
        fields = ('id', 'first_name', 'last_name', 'parent')


