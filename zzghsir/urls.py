# -*- coding: gbk -*-
from django.conf.urls import*
from django.contrib import admin
from register import views
from zzghsir import settings
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'self1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^mainInterface/$',views.mainInterface),
    url(r'^login/$',views.loginInterface),
    url(r'^loginVerify/$',views.loginVerify),
    url(r'^register/$',views.register),
    url(r'^RegisterService/$',views.RegisterServiceInterface),
    url(r'^appointManage/$',views.appointManageIntereface),
    url(r'^about/$',views.aboutIntereface),
    

    url(r'^detailInformation/(.+)/$',views.detailInformation),
    url(r'^order/(.+)/$',views.order),
    url(r'^exit/$',views.exitApp),
    
    url(r'^deleteDoctor/$',views.deleteAppointDoctor),
    
    
    url(r'^PchangePasswordSuccess/$',views.PchangePasswordSuccess),
    url(r'^PchangePassword/(.+)/$',views.PchangePassword),
    url(r'^updataPatientInfoSuccess/$',views.updataPatientInfoSuccess),
    url(r'^PchangeSelfInfo/$',views.PchangeSelfInfo),
    url(r'^patientHome/$',views.patientHome),
    
    url(r'^doctorHome/(.+)/$',views.doctorHome),
    url(r'^changeSelfInfo/(.+)/$',views.changeSelfInfo),
    url(r'^updataDoctorInfoSuccess/$',views.updataDoctorInfoSuccess),
    url(r'^DchangePassword/(.+)/$',views.DoctorchangePassword),
    url(r'^DchangePasswordSuccess/$',views.DchangePasswordSuccess),
    url(r'^returnAppointList/(.+)/$',views.returnAppointList),
    url(r'^doctorExit/$',views.doctorExitApp),

    #按条件查询
    url(r'^demandByDoctor/$',views.demandByDoctor),
    url(r'^demandAllDoctor/$',views.demandAllDoctor),    
    url(r'^demandByDivision/$',views.demandByDivision),
    url(r'^demandByIllness/$',views.demandByIllness),
    
    #管理新闻资讯
    url(r'^register/updataNews/$',views.updataNews),
    url(r'^createNews/$',views.createNews),
    url(r'^saveNews/$',views.saveNews),
    url(r'^deleteNews/(.+)/$',views.deleteNews),
    url(r'^showNews/(.+)/$',views.showNews),

    url(r'^news1/$',views.news1),
    url(r'^news2/$',views.news2),
    url(r'^news3/$',views.news3),

    url(r'^problem1/$',views.problem1),
    url(r'^problem2/$',views.problem2),
    #管理科室    
    url(r'^register/manageDivision/$',views.manageDivisionInterface),
    url(r'^addDivision/$',views.addDivision),
    url(r'^showDivision/$',views.showDivision),
    url(r'^deleteDivision/(.+)/$',views.deleteDivision), 
    
    #管理疾病库
    url(r'^register/illnessLibrary/$',views.illnessLibrary),
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
    
    
    
    
    
    #url(r'^static/(?P<path>.*)$','staticeview.static.serve',{'document_root':settings.STATIC_ROOT},name = "static")    
    #url(r'^media/(?P<path>.*)$','staticeview.static.serve',{'document_root':settings.STATICFILES_DIRS,'show_indexes': True}),
)
    #urlpatterns += patterns(
       # url(r'^static/(?P<path>.*)$',statceview.static.serve,{'document_root':settings.STATIC_ROOT},name = "static")    
        #url(r'^media/(?P<path>.*)$',statceview.static.serve,{'document_root':settings.MEDIA_ROOT},name = "media") 
    #)




