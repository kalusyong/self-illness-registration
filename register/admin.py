from django.contrib import admin
from register.models import*
from django.conf.urls import*
# Register your models here.
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('divisionID','name')
    search_fields = ('divisionID','name')
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('userName','Password','userCategory','name','age',
                    'sex','phoneNumber','intro','division','workTime',
                    'appointedPerson','appointNum')
    search_fields = ('userName','Password','userCategory','name','age',
                    'sex','phoneNumber','intro','division')
    raw_id_fields = ('division',)
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ('userName','Password','userCategory','name','age',
                    'sex','phoneNumber')
    search_fields = ('userName','Password','userCategory','name','age',
                    'sex','phoneNumber')
    
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('userName','Password','userCategory')
    search_fields = ('userName','Password','userCategory')
    
class IllnessAdmin(admin.ModelAdmin):
    list_display = ('name','division')
    search_fields = ('name','division')
    raw_id_fields = ('division',)
    filter_horizontal = ('doctor',)
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('Title','Text','Image','author','Data')
    search_fields = ('Title','Text','Image','author','Data')
    
class appointTableAdmin(admin.ModelAdmin):
    list_display = ('patient','weekNumber','appintDate')
    search_fields = ('patient','weekNumber','appintDate')
    raw_id_fields = ('patient',)
    filter_horizontal = ('doctorList',)
admin.site.register(Division,DivisionAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Illness,IllnessAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(appointTable,appointTableAdmin)