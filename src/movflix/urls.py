from django.contrib import admin
from django.urls import path

from playlists.views import MovieListView, TVShowListView, FeaturedPlaylistListView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', FeaturedPlaylistListView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('shows/', TVShowListView.as_view()),
]
