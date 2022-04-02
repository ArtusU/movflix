from django.contrib import admin
from django.urls import path, include

from playlists.views import (
    MovieListView, 
    TVShowListView, 
    FeaturedPlaylistListView, 
    MovieDetailView, 
    PlaylistDetailView,
    TVShowSeasonDetailView,
    TVShowDetailView
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', FeaturedPlaylistListView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<slug:slug>/', MovieDetailView.as_view()),
    path('movies/', MovieListView.as_view()),
    
    path('media/<int:pk>/', PlaylistDetailView.as_view()),
    
    # path('category/', include('categories.urls')),
    # path('categories/', include('categories.urls')),
    
    # path('search/', SearchView.as_view()),
    
    path('shows/<slug:showSlug>/seasons/<slug:seasonSlug>/', TVShowSeasonDetailView.as_view()),
    path('shows/<slug:slug>/seasons/', TVShowDetailView.as_view()),
    # path('shows/<slug:slug>/', TVShowDetailView.as_view()),
    path('shows/', TVShowListView.as_view()),
    
    # path('tags/', include('tags.urls')),
    # path('object-rate/', rate_object_view)
]
