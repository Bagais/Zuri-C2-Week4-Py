from django.db import models

# Create your models here.

class Artiste(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField()
	# id = models.BigAutoField(primary_key=True)


	#specifying the tag for the artiste model.
	#The "first_name" assigned to the input will 
	#serve as the title for the entry.
	def __str__(self):
		return self.first_name

class Song(models.Model):
	title = models.CharField(max_length=30)
	date_released = models.DateField()
	likes = models.IntegerField()
	artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
	# id = models.BigAutoField(primary_key=True)


	def __str__(self):
		return self.title


class Lyric(models.Model):
	content = models.CharField(max_length=10000)
	song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
	# id = models.BigAutoField(primary_key=True)


	def __str__(self):
		return self.content


