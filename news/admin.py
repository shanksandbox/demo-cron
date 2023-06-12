from django.contrib import admin
from .models import HackerNewsID


class HackerNewsIDAdmin(admin.ModelAdmin):
    list_display = ('hackernews', 'fetched_at') #these are the features to be listed
    list_display_links = ('hackernews', 'fetched_at') #these are the features links

admin.site.register(HackerNewsID, HackerNewsIDAdmin)