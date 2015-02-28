from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(regex=r'^',
        view=include('myblog.urls')),

    url(regex=r'^login/$',
        view='django.contrib.auth.views.login',
        kwargs={'template_name': 'login.html'},
        name="login"),

    url(regex=r'^logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={'next_page': '/'},
        name="logout"),

    url(regex=r'^admin/',
        view=include(admin.site.urls)),
)
