from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from pyrio.eventos import views as eventos_view

urlpatterns = [
    url(r'^$', eventos_view.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', eventos_view.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
