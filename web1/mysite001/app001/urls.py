from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[
    #url(r'^$',views.test1,name='test1'), # app001首页显示“确定”按钮
    #url(r'^/test1/',views.index1,name='index1'), # 匹配点击后传递回来的url
    url(r'^index/$',views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#符号 $ 表示尾部匹配，再加上符号 ^ （头部匹配），^$表示匹配首页。
#这里我们建立了一个url和view的关系，即在首页地址“http://XXX/app001”页面上显示视图index1。
