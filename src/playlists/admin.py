from django.contrib import admin

# Register your models here.
from .models import TVShowProxy, TVShowSeasonProxy, Playlist, PlaylistItem


class SeasonEpisodeInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0

class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [SeasonEpisodeInline]
    list_display = ['title', 'parent']
    class Meta:
        model = TVShowSeasonProxy
    
    def get_queryset(self, request):
        return TVShowSeasonProxy.objects.all()

admin.site.register(TVShowSeasonProxy, TVShowSeasonProxyAdmin)


class TVShowSeasonProxyInline(admin.TabularInline):
    model = TVShowSeasonProxy
    extra = 0
    fields = ['order', 'title', 'state']

class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TVShowSeasonProxyInline]
    list_display = ['title']
    fields = ['title', 'description', 'state', 'video', 'slug']
    class Meta:
        model = TVShowProxy
    
    def get_queryset(self, request):
        return TVShowProxy.objects.all()

admin.site.register(TVShowProxy, TVShowProxyAdmin)


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInline]
    class Meta:
        model = Playlist

admin.site.register(Playlist, PlaylistAdmin)