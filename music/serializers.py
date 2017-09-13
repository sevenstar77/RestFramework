from rest_framework import serializers
from music.models import Music

# class MusicSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     release_date = serializers.DateTimeField()
#
#     music_category = serializers.CharField(max_length=200)
#     played = serializers.BooleanField(required=False)
#
#     def create(self, validated_data):
#         return Music.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', validated_data.name)
#         instance.validated_data = validated_data('release_date', validated_data.release_date)
#         instance.music_category = validated_data.get('music_category', validated_data.music_category)
#         instance. played = validated_data.get('played', validated_data.played)
#         instance.save()
#
#         return instance

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = (
            'id',
            'name',
            'release_date',
            'music_category',
            'played'
        )
