#from django.conf.urls import url
#from .views import HelloView
#from django.urls import path
#from django.urls.resolvers import URLPattern
#from django.urls import path
#from . import views #.は記述しているファイルの属するフォルダ
from django.urls import path
from . import views
from .views import FriendList
from .views import FriendDetail



urlpatterns = [
    path('',views.index,name='index'),
    path('<int:num>',views.index,name='index'),
    path('create',views.create,name='create'),
    path('edit/<int:num>',views.edit,name='edit'),
    path('delete/<int:num>',views.delete,name='delete'),
    path('find',views.find,name='find'),
    path('list',FriendList.as_view()),
    path('detail/<int:pk>',FriendDetail.as_view()),
    path('check',views.check,name='check'),
    path('message/',views.message,name='message'),    
    path('message/<int:page>',views.message,name='message')
]