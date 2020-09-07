from django.contrib import admin

from .models import Artist, Gallery, Exhibition, Painting, Exhibition_Painting

# Register your models here.
admin.site.register(Artist)
admin.site.register(Gallery)
admin.site.register(Exhibition)
admin.site.register(Painting)
admin.site.register(Exhibition_Painting)
