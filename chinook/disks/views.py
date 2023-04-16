from django.shortcuts import render,get_list_or_404,get_object_or_404

from .models import Album

def albums(request):
    albums = get_list_or_404(Album)
    return render(request,'disks/albums.html',{'albums':albums})

def album_details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request,'disks/album_details.html',{'album':album})
