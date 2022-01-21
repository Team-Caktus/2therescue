from rest_framework import serializers
from .models import Foster, Tag, Pet


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


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('breed',
        'age',
        'size',
        'description',
        'vac_status',
        'image_url',
        'spay_neuter',
        'health_notes',
        'tags',
        'notes',
        'date_created',
        'date_updated',
        )
