from django.urls import path,include
from .views import home,dowload


urlpatterns = [
    path("", home, name="home"),
    path('download',dowload,name='download')
]