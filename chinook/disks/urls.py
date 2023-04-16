from django.urls import path

from . import views

app_name = 'disks'

urlpatterns = [
    path('', views.albums, name='albums'),
    path('<int:album_id>/', views.album_details, name='album_details')
]