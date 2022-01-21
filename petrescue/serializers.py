from rest_framework import serializers
from .models import Foster, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag')

class FosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foster
        fields = ('first_name',
        'last_name',
        'address',
        'email',
        'num_of_adults',
        'ages_of_children',
        'any_other_pets',
        )
