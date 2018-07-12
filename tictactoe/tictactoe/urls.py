"""
Definition of urls for tictactoe.
"""

from django.conf.urls import include, url
from .views import welcome

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^player/', include('player.urls')),
    url(r'^$', welcome, name='tictactoe_welcome'),
    url(r'^games/', include('gameplay.urls'))
    
    # Examples:
    # url(r'^$', tictactoe.views.home, name='home'),
    # url(r'^tictactoe/', include('tictactoe.tictactoe.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
