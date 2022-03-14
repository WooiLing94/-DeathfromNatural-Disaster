# from django.conf.urls import url
from combine import views
from django.conf import settings
from django.urls import include, re_path 
from django.conf.urls.static import static

app_name = 'combine'

urlpatterns=[
    re_path('',views.HomePageView.as_view(), name='home'),
    re_path('getFloods/',views.Api.getFloods, name='get-floods'),
    re_path('getFloods/',views.Api.getFloods, name='get-wildfire'),
    re_path('getStorms/',views.Api.getStorms, name='get-storms'),
    re_path('getLandslides/',views.Api.getLandslides, name='get-landslides'),
    re_path('getEarthquakes/',views.Api.getEarthquakes, name='get-earthquakes')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)