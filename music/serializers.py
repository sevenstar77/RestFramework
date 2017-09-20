from rest_framework import serializers
from music.models import Music
from music.models import MusicCategory
from music.models import Player
from music.models import PlayerScore

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

# class MusicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Music
#         fields = (
#             'id',
#             'name',
#             'release_date',
#             'music_category',
#             'played'
#         )

class MusicCategorySerializer(serializers.HyperlinkedModelSerializer):
    musics = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='music-detail')

    class Meta:
        model = MusicCategory
        fields = (
            'url',
            'pk',
            'name',
            'musics'
        )

class MusicSerializer(serializers.HyperlinkedRelatedField):
    music_category = serializers.SlugRelatedField(queryset=MusicCategory.objects.all(), slug_field='name')

    class Meta:
        model = Music
        fields = (
            'url',
            'music_category',
            'name',
            'release_date',
            'played'
        )

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    music = MusicSerializer()

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'music',
        )

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    socres = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display',read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
        )

class PlayerScoreSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                          slug_field='name')
    music = serializers.SlugRelatedField(queryset=Music.objects.all(),slug_field='name')

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'music',
        )
