from rest_framework import serializers

from cosplay_project.store.models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
