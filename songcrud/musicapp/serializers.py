from rest_framework import serializers
from .models import Artiste, Song, Lyric


class ArtisteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste
		fields = ['id', 'first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste
		fields = ['id', 'title', 'date_released', 'likes']

class LyricSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste
		fields = ['id', 'content']