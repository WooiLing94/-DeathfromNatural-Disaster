from django.urls import include, re_path 
from homePage import views

app_name = 'homePage'

urlpatterns=[
    re_path(r'^register/$',views.register,name='register'), #url name
    re_path(r'^user_login/$',views.user_login,name='user_login'),
    re_path(r'^dashboard/$',views.dashboard,name='dashboard'),
    re_path(r'^analysis/$',views.analysis,name='analysis'),
]