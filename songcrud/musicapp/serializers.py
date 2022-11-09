from rest_framework import serializers
from .models import Artiste, Song, Lyric


class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artiste
		fields = ('first_name', 'last_name', 'age')

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste
		fields = ('title', 'date_released', 'likes', 'artiste_id')

class LyricSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste
		fields = ('content', 'song_id')