from django.conf.urls import url
from houdasfirstapp import views

 # this looks for the index function in views
urlpatterns = [
    url(r'^$', views.index, name='index'), #$ means it went to firstapp by default

    url(r'^(?P<picture_id>[0-9]+)/$', views.detail, name='detail'),

]

