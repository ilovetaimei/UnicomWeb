"""JCSSJK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from jc import views
from jc import dao
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jk/',views.jk),
    url(r'^mo/',dao.selectmotorroom),
    url(r'^wa/',views.warninglog),
    url(r'^eq/$',views.details),
    url(r'^qr/$',views.portdescript),
    url(r'^op/$',views.nowerror,name='nowerror'),
    url(r'^gp/$',dao.selectgroup),
    url(r'^mp/$',views.mainop),
    url(r'^qp/$',views.querymp),
    url(r'^ad/$',dao.addping),
    url(r'^np/$',dao.neteqop),
    url(r'^index/$',views.index),
    url(r'^netreport/$',views.netport),
    url(r'^quarynetreport/$',views.quarynetreport),
    url(r'^netportdetails/$',views.netreport),
    url(r'^netportdata/$', views.netreportdata),
    url(r'^pingreportdata/$', views.pingreport),

]
