from django.contrib import admin
from django.urls import include, re_path 
from homePage import views
from naturalDisaster.settings import DEBUG, STATIC_URL, STATIC_DIR, MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$',views.index,name='index'),
    re_path(r'^special/',views.special,name='special'),
    re_path(r'^homePage/',include('homePage.urls')),
    re_path(r'^combine/',include('combine.urls')),
    re_path(r'^logout/$',views.user_logout, name='logout')
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)