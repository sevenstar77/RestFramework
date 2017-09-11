from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from music.models import Music
from music.serializers import MusicSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
    def music_list(request):
        if request.method == 'GET':
            musics = Music.objects.all()
            musics_serializer = MusicSerializer(data=musics, many=True)
            return JSONResponse(musics_serializer)

        elif request.method == 'POST':
            music_data = JSONParser().parse(request)
            music_serializer = MusicSerializer(data=music_data)

            if music_serializer.is_valid():
                music_serializer.save()
                return JSONResponse(music_serializer.data, status=status.HTTP_201_CREATED)
            return JSONResponse(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def music_detail(request, pk):
        try:
            music = Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            music_serializer = MusicSerializer(music)
            return JSONResponse(data=music_serializer.data)
        elif request.method == 'POST':
            music_data = JSONParser.parse(request)
            music_serializer = MusicSerializer(music, data=music_data)
            if music_serializer.is_valid():
                music_serializer.save()
                return JSONResponse(music_serializer.data)
            return JSONResponse(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            music.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)





