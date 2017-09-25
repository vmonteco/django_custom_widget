from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="main/home.html"), name='home'),
    url(r'^pictures/$', views.PictureListView.as_view(), name='picture_list'),
    url(r'^pictures/(?P<pk>\d+)/$', views.PictureDetailView.as_view(), name='picture_detail'),
    url(r'^pictures/(?P<pk>\d+)/update/$', views.PictureUpdateView.as_view(), name='picture_update'),
    url(r'^pictures/create/$', views.PictureCreateView.as_view(), name='picture_create'),
    url(r'^pictures/(?P<pk>\d+)/delete/$', views.PictureDeleteView.as_view(), name='picture_delete'),
    url(r'^lists/$', views.ListListView.as_view(), name='list_list'),
    url(r'^lists/(?P<pk>\d+)/$', views.ListDetailView.as_view(), name='list_detail'),
    url(r'^lists/(?P<pk>\d+)/update/$', views.ListUpdateView.as_view(), name='list_update'),
    url(r'^lists/create/$', views.ListCreateView.as_view(), name='list_create'),
    url(r'^lists/(?P<pk>\d+)/delete/$', views.ListDeleteView.as_view(), name='list_delete'),
]
