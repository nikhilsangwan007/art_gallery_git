from django.db import models

# Create your models here.
class Artist(models.Model):
	artist_id = models.IntegerField(primary_key=True)
	artist_name = models.CharField(max_length=200)
	birthplace = models.CharField(max_length=200)
	art_type = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	def __str__(self):
		return '%d %s' % (self.artist_id, self.artist_name)

class Painting(models.Model):
	painting_id = models.IntegerField(primary_key=True)
	artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_id_fk')
	painting_name = models.CharField(max_length=200)
	genre = models.CharField(max_length=200)
	year_of_publish = models.DateField()
	price = models.IntegerField()
	rating = models.IntegerField()
	painting_url = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	def __str__(self):
		return '%d %s' % (self.painting_id, self.painting_name)

class Gallery(models.Model):
	gallery_id = models.IntegerField(primary_key=True, null=False)
	gallery_name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	def __str__(self):
		return '%d %s' % (self.gallery_id, self.gallery_name)

class Exhibition(models.Model):
	exhibition_id = models.IntegerField(primary_key=True, null=False)
	exhibition_name = models.CharField(max_length=200)
	gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery_id_fk')
	start_date = models.DateField()
	end_date = models.DateField()
	def __str__(self):
		return '%d %s' % (self.exhibition_id, self.exhibition_name)

class Exhibition_Painting(models.Model):
	painting_id = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name='painting_id_fk')
	exhibition_id = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='exhibition_id_fk')
	
	class Meta:
		unique_together = (('painting_id', 'exhibition_id'),)
	
	def __str__(self):
		return '%d %s' % (self.painting_id, self.exhibition_id)
