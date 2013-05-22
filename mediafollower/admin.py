from django.contrib import admin
from mediafollower.models import * 

#class MediaAdmin(admin.ModelAdmin):
#  date_heirarchy

admin.site.register(Media)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(UserProfile)
admin.site.register(Media_Request)
