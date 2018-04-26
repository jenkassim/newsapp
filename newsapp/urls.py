from django.conf.urls import url
from newsapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^settings$', views.SourceList.as_view(), name='source_list'),
    url(r'^add$', views.SourceCreate.as_view(), name='source_add'),
    url(r'^edit/(?P<pk>\d+)$', views.SourceUpdate.as_view(), name='source_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.SourceDelete.as_view(), name='source_delete'),
    url(r'^view$', views.feed_list, name='feed_list'),
    url(r'^detail/(?P<pk>\d+)$', views.FeedDetailView.as_view(), name='feed_detail'),
    url(r'^parse$', views.feed_refresh, name='feed_refresh'),
    url(r'^clear$', views.feed_delete_all, name='feed_delete'),
    ]

