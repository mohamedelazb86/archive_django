from django.urls import path
from . import views

app_name='settings'


urlpatterns = [
    path('',views.base,name='base'),

    path('sector',views.sector,name='sector'),
    path('add-sector',views.add_sector,name='add_sector'),
    path('delete-sector',views.delete_sector,name='delete-sector'),
    path('edit-sector',views.edit_sector,name='edit-sector'),

    path('contractor',views.sector,name='contractor'),
    path('document_type',views.sector,name='document_type'),

]
