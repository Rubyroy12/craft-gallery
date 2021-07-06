from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns =[
    url('^$', views.home, name='homepage'),
    url('^gallery/', views.gallery, name='gallery'),
    url('^gallery/<int:image_id>/$', views.single_image, name='image_details'),
    url('^category/technology/$',views.technology, name='technology'),
    url('^category/nature/$',views.nature, name='nature'),
    url('^category/meditation/$',views.meditation, name='meditation'),
    url('location/$',views.image_location, name='location'),
    url('search/$', views.search_results, name='search_results'),
    url('^about/', views.about,name='about'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)