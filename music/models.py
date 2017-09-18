from django.db import models

# Create your models here.

# class Music(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=200, blank=True, default='')
#     release_date = models.DateTimeField()
#     music_category = models.CharField(max_length=200, blank=True, default='')
#     played = models.BooleanField(default=False)
#
#     class Meta:
#         ordering=('name',)

class MusicCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class Music(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    music_category = models.ForeignKey(
        MusicCategory,
        related_name='musics',
        on_delete=models.CASCADE
    )
    release_date = models.DateTimeField()
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
            return self.name

class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player,
        related_name='scores',
        on_delete=models.CASCADE
    )
    music = models.ForeignKey(
        Music,
        on_delete=models.CASCADE
    )
    socre = models.IntegerField()
    socre_date = models.DateTimeField()

    class Meta:
        ordering = ('-socre',) #  - 내림차순
