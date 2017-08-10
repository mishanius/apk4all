"""hen4us URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/search/$', views.topApps.as_view(), name="API"),
    url(r'api/search/(?P<pk>.+)', views.Search.as_view(), name="API"),
    url(r'api/itm/(?P<name>.*)', views.GetItem.as_view(), name="GetItem"),
    url(r'api/itm/', views.GetItem.as_view(), name="GetItem"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
