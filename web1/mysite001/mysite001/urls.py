"""mysite001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include #增加include
from django.contrib import admin

urlpatterns = [
    url(r'^',include('app001.urls')), # 增加对应关系
    url(r'^admin/', admin.site.urls),
]

#正则表达式 r'^app001'，符号 ^ 表示头部匹配。
#整段语句表示，若网站地址为"http://XXXXX/app001……" ，则该地址分配到"app001/urls.py"文件来处理。
