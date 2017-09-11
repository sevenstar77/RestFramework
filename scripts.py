from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from music.models import Music
from music.serializers import MusicSerializer

musicdatetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
# music = Music(name='dh', release_date=musicdatetime, music_category='hip-hop', played=False)
# music.save()
#
# musicV2 = Music(name='tiger', release_date=musicdatetime, music_category='k-pop', played=False)
# musicV2.save()

musicV3 = Music(name='max', release_date=musicdatetime, music_category='ballad', played=False)
musicV3.save()

music3Serializer = MusicSerializer(musicV3)
print(music3Serializer.data)

renderer = JSONRenderer()
rendered_data1 = renderer.render(music3Serializer)



