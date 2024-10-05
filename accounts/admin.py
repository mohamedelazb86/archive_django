from django.contrib import admin

from accounts.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','image']
    list_filter=['']
    search_fields=['user']

admin.site.register(Profile)

