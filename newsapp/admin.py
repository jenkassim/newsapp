from django.contrib import admin
from .models import NewsFeed, NewsSource

# Register your models here.
admin.site.register(NewsFeed)
admin.site.register(NewsSource)