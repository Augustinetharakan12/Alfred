"""excelreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from register.views import regview,offlinereg,paidreg,SearchByView,schoolreg
from controlroom.views import ControlRoomView
from controlroom.views import Eventview
from register.views import certi
from controlroom.views import postcreate,android,venuedetail,Download,venueupdate,winnerapi,eventnav,intermediate,winnerDownload

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^online/$',regview.as_view(),name='home'),
    url(r'^paidreg/$',paidreg.as_view(),name='paidreg'),
    url(r'^offlinereg/$',offlinereg.as_view(),name='offline'),
    url(r'^studentreg/$',schoolreg.as_view(),name='stud'),
    url(r'^controlroom/$',ControlRoomView.as_view(),name='controlroom'),
    url(r'^eventpage/(?P<event>[\w,()-]+)/$',Eventview.as_view(),name='eventview'),
    url(r'^eventpage/$',intermediate,name='eventview'),
    url(r'^eventnav/$',eventnav.as_view(),name='eventnav'),
    url(r'^venuepage/(?P<venue>[\w,()-]+)/$',venuedetail.as_view(),name='venueview'),
    url(r'^certificate/$',certi,name='certificate'),
    url(r'^searchby/$',SearchByView.as_view(),name='searchby'),
    url(r'^eventpage/(?P<pk>[\w,()-]+)/create/$',postcreate,name='controolroom'),
    url(r'^venuepage/(?P<ven>[\w,()-]+)/create/$',venueupdate.as_view(),name='venupdate'),
    url(r'^eventpage/(?P<eve>[\w,()-]+)/download/$',Download.as_view(),name='down'),
    url(r'^eventpage/(?P<eve>[\w,()-]+)/winnerdownload/$',winnerDownload.as_view(),name='windown'),
    url(r'^api/(?P<pk>[\w,()-]+)',android.as_view(),name='api'),
    url(r'^winnerapi/(?P<pk>[\w,()-]+)',winnerapi.as_view(),name='winnerapi')
]
