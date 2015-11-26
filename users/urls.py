from django.conf.urls import include, url
from . import views

urlpatterns = [

# url(r'^$', views.home),


url(r'^users/(?P<nombre>\w+)$',views.usuarios),
url(r'^users/get/(?P<id>\d+)$',views.dar_usuario),

]
