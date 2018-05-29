from django.conf.urls import patterns, include, url
from django.contrib import admin
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'income_manage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'income_manage_app.views.home'),
    # url(r'^insertdata/$', 'income_manage_app.views.insertdata'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', xadmin.site.urls),
)
