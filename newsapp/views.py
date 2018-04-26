from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm

from .models import NewsSource, NewsFeed
import feedparser

def index(request):
    return render(request, 'index.html')

class SourceList(ListView):
    model = NewsSource

class SourceCreate(CreateView):
    model = NewsSource
    success_url = reverse_lazy('source_list')
    fields = ['source_name', 'source_perc', 'source_link']

class SourceUpdate(UpdateView):
    model = NewsSource
    success_url = reverse_lazy('source_list')
    fields = ['source_name', 'source_perc', 'source_link']

class SourceDelete(DeleteView):
    model = NewsSource
    success_url = reverse_lazy('source_list')

class FeedDetailView(DetailView):
    queryset = NewsFeed.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def feed_list(request):
    feeds = NewsFeed.objects.all().order_by('source')
    source = NewsSource.objects.all()
    context = {'feeds': feeds, 'source': source}
    return render(request, 'newsapp/newsfeed_list.html', context)

def feed_delete_all(request):
    obj = NewsFeed()
    obj.delete_all_news()
    success_url = reverse_lazy('feed_list')
    return render(request, 'newsapp/newsfeed_list.html')

def feed_refresh(request):
    sites_dict = NewsSource.objects.all().values().order_by('id')
    context = {}
    total = {}
    max_feed = 30

    for site in sites_dict:
        src  = NewsSource.objects.get(id=site['id'])
        url  = src.source_link
        perc = src.source_perc
        s_id = site['id']

        data = feedparser.parse(url)
        max_entries = len(data['entries'])
        limit = int(perc * max_feed / 100)

        if limit > max_entries:
            limit = max_entries

        for i in range(0, limit):
            feed = src.newsfeed_set.create(
                title = data['entries'][i]['title'],
                content = data['entries'][i]['summary'],
                content_link = data['entries'][i]['link']
            )

        total[src.source_name] = limit

    context = { 'total': total }
    return render(request, 'newsapp/newsfeed_form.html', context)