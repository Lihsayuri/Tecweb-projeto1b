from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='note_delete'),
    path('edit/<int:id>', views.edit, name='note_edit'),
    path('tags', views.index_tag, name='tag_get'),
    path('tag/<int:tagid>', views.tag_details, name='tag_details')
]