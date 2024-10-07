from django.contrib import admin

from .models import Document_Type,Sector,Contractor

class SectorAdmin(admin.ModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']
    

admin.site.register(Document_Type)
admin.site.register(Sector,SectorAdmin)
admin.site.register(Contractor)
