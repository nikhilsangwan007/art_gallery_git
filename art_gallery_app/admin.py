from django.contrib import admin

from .models import DbArtist, DbExhibition, DbExhibitionPainting, DbGallery, DbPainting

# Register your models here.
admin.site.register(DbArtist)
admin.site.register(DbGallery)
admin.site.register(DbExhibition)
admin.site.register(DbPainting)
admin.site.register(DbExhibitionPainting)
