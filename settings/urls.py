from django.urls import path
from . import views

app_name='settings'


urlpatterns = [
    path('',views.base,name='base'),

    path('sector',views.sector,name='sector'),
    path('add-sector',views.add_sector,name='add_sector'),
    path('delete-sector',views.delete_sector,name='delete-sector'),
    path('edit-sector',views.edit_sector,name='edit-sector'),

    path('contractor',views.contractor,name='contractor'),
    path('add-contractor',views.add_contractor,name='add-contractor'),
    path('delete-contractor',views.delete_contractor,name='delete-contactor'),
    path('edit-contractor',views.edit_contractor,name='edit-contractor'),


    path('document_type',views.document_type,name='document_type'),
    path('add-document_type',views.add_document_type,name='add-document-type'),
    path('delete-document_type',views.delete_document_type,name='delete-document-type'),
    path('edit-document-type',views.edit_document_type,name='edit-document-type'),

]
