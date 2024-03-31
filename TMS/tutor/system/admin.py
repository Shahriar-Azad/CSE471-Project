from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TutorDetail)


from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Data)