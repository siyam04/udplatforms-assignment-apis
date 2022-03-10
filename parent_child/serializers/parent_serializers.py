from rest_framework import serializers

# App related
from parent_child.models import Parent


# Parent List Serializer
class ParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


