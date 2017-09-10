from django.db import models

# Create your models here.

class Music(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    reloease_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        ordering=('name',)