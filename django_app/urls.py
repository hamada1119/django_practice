from django.contrib import admin
#from django.contrib.auth import default_app_config
from django.urls import path,include
from rest_framework import routers
from sns.views import MessageViewset

defaultRouter=routers.DefaultRouter()#DefaultRouterクラスのインスタンスを代入
defaultRouter.register(
    'Message',
    MessageViewset
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',include('hello.urls')),
    path('api/',include(defaultRouter.urls))
]
