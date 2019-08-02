from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.home,name='home'),
    url(r'register',views.register,name= 'signup'),
    url(r'^search/', views.search_project, name='search'),
    url(r'^newproject',views.add_project, name = "addproject")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)