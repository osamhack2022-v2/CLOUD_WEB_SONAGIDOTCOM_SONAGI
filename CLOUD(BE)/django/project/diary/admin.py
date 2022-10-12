from django.contrib import admin

# Register your models here.
from .models import diary

class DiaryAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(diary, DiaryAdmin)