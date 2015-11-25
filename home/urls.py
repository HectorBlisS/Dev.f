from django.conf.urls import include, url
from . import views

urlpatterns = [

# url(r'^$', views.home),

url(r'^(?P<number1>\d)/(?P<number2>\d)$',views.home),
url(r'^hola',views.hello),

]
