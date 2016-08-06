from django.contrib import admin

# Register your models here.
from Profile.models import Comments, Follow, Likes, Image

admin.site.register(Comments)
admin.site.register(Image)
admin.site.register(Likes)
admin.site.register(Follow)