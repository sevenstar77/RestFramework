from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
#추가 api_view를 이용할 경우 http_method_names 인자로 들어가면 지원하지 않는 http동사가 들어올경우 데커레이터가 처리해주기
#때문에 예기치 않은 오류를 발생 시키지 않을 수 있다.

from music.models import Music
from music.serializers import MusicSerializer

# Create your views here.
#기존 JSONResponse 를 이용해서 사용한 방법
# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#     @csrf_exempt
#     def music_list(request):
#         print(request.method)
#         if request.method == 'GET':
#             musics = Music.objects.all()
#
#             music_serializer = MusicSerializer(musics, many=True)
#             #many = True 인자로 지정하여 사용하면 여러 인스턴스를 직렬화할 것을 지정하게 됨
#             #many 인자 값을 True로 설정하면 장고는 내부적으로 ListSerializer를 사용한다..
#             return JSONResponse(music_serializer.data)
#
#         elif request.method == 'POST':
#             # music_data = JSONParser().parse(request)
#             # music_serializer = MusicSerializer(data=music_data)
#
#             #json 이 아닌 다른 content-type을 대비해야 할 경우
#             music_serializer = MusicSerializer(data=request.data)
#
#             if music_serializer.is_valid():
#                 music_serializer.save()
#                 return JSONResponse(music_serializer.data, status=status.HTTP_201_CREATED)
#             return JSONResponse(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     @csrf_exempt
#     def music_detail(request, pk):
#         try:
#             music = Music.objects.get(pk=pk)
#         except Music.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'GET':
#             music_serializer = MusicSerializer(music)
#             return JSONResponse(data=music_serializer.data)
#
#         elif request.method == 'POST':
#             # music_data = JSONParser.parse(request)
#             # music_serializer = MusicSerializer(music, data=music_data)
#             # json 이 아닌 다른 content-type을 대비해야 할 경우
#             music_serializer = MusicSerializer(music, data=request.data)
#
#             if music_serializer.is_valid():
#                 music_serializer.save()
#                 return JSONResponse(music_serializer.data)
#             return JSONResponse(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         elif request.method == 'DELETE':
#             music.delete()
#             return HttpResponse(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        music_serializer = MusicSerializer(musics, many=True)
        return Response(music_serializer.data)

    elif request.method == 'POST':
        music_serializer = MusicSerializer(data=request.data)
        if music_serializer.is_valid():
            music_serializer.save()
            return Response(music_serializer.data, status=status.HTTP_201_CREATED)

        return Response(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





