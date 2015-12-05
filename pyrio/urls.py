from django.conf.urls import url
from django.contrib import admin

from pyrio.eventos import views as eventos_view

urlpatterns = [
    url(r'^$', eventos_view.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]
