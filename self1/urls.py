# -*- coding: gbk -*-
from django.conf.urls import*
from django.contrib import admin
from register import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'self1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^mainInterface/$',views.mainInterface),
    url(r'^login/$',views.loginInterface),
    url(r'^loginVerify/$',views.loginVerify),
    url(r'^register/$',views.register),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demandDoctor/$',views.demandDoctor),
    url(r'^detailInformation/(.+)/$',views.detailInformation),
    url(r'^order/(.+)/$',views.order),
    url(r'^signOut/$',views.signOut),
    url(r'^appointManage/$',views.appointManageIntereface),
    url(r'^deleteDoctor/(.+)/$',views.deleteAppointDoctor),   
    url(r'^register/illnessLibrary/$',views.illnessLibrary),
    
    
    url(r'^register/updataNews/$',views.updataNews),
    url(r'^createNews/$',views.createNews),
    url(r'^saveNews/$',views.saveNews),
    url(r'^deleteNews/(.+)/$',views.deleteNews),
    url(r'^showNews/(.+)/$',views.showNews),
    #管理科室    
    url(r'^register/manageDivision/$',views.manageDivisionInterface),
    url(r'^addDivision/$',views.addDivision),
    url(r'^showDivision/$',views.showDivision),
    url(r'^deleteDivision/(.+)/$',views.deleteDivision), 
    
    #管理疾病库
    url(r'^register/illnessLibrary/addIllness/$',views.addIllness),    
    url(r'^register/illnessLibrary/addIllness/illnessAddDoctor/$',views.illnessAddDoctor),
    url(r'^addIllnessSuccess/$',views.addIllnessSuccess),
    url(r'^addIllnessSuccess/illnessAddDoctor/$',views.illnessAddDoctor),
    url(r'^register/illnessLibrary/addIllness/illnessAddDoctor/illnessAddDoctor/$',views.illnessAddDoctor),
    url(r'^updataIllnessInfo/$',views.updataIllnessInfo),
    url(r'^updataIllnessByName/$',views.updataIllnessByName),
    url(r'^updataIllnessByDivision/$',views.updataIllnessByDivision),
    url(r'^deleteIllness/(.+)/$',views.deleteIllness),
    url(r'^illnessDetailInfo/(.+)/$',views.illnessDetailInfomation),    
    url(r'^updataIllnessSuccess/$',views.updataIllnessSuccess),
    
    
    url(r'^demandDivision/$',views.demandDivision),
    url(r'^demandIllness/$',views.demandIllness),
    url(r'^registraService/$',views.registraServiceInterface),
    
    url(r'^newMassage/$',views.newMassageInterface),
    
)
