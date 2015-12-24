# -*- coding: gbk -*-
from django.shortcuts import*
from register import models
from django.http import HttpResponse,HttpResponseRedirect
from PIL import Image
#import time
import datetime
# Create your views here.
loginPatient = models.Patient()
loginPatient.userName = 'login'
loginDoctor = models.Doctor()
loginDoctor.userName = 'login'
URL = "/mainInterface/"

weekday = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
weekdayRever = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}

now = datetime.datetime.now()
now = now.date()
now = now + datetime.timedelta(hours=24)
datelist = {now:weekday[now.isoweekday()]}
for i in range(1,7):
    now = now + datetime.timedelta(hours=24)
    datelist[now] = weekday[now.isoweekday()]
    i = i+1
datesort = sorted(datelist.iteritems(), key = lambda asd:asd[0], reverse = False)

class date():
    dates = 0
    week = 0
    
datesorts=[]
for i in range(0,7):
    team = date()
    team.dates = datesort[i][0].isoweekday()
    datesort[i] = list(datesort[i])
    datesort[i][0] = str(datesort[i][0])
    team.week = datesort[i][0] + '(' + datesort[i][1] + ')'
    datesorts.append(team)

#login = loginPatient
#loginPatient = models.Patient.objects.filter(userName = '��¼')

def mainInterface(request):
    global loginPatient
    divisionList = models.Division.objects.all()
    return render_to_response('mainInterface.html',
                              {'login': loginPatient.userName,"divisionList":divisionList})
def loginInterface(request):
    allDivisionList = models.Division.objects.all()
    return render_to_response('login.html',
                             {"allDivisionList":allDivisionList})
def illnessLibrary(request):
    return render_to_response('illnessLibrary.html')
def manageDivisionInterface(request):
    return render_to_response('manageDivision.html')
def addIllness(request):
    divisionList = models.Division.objects.all()
    return render_to_response("addIllness.html",{'divisionList':divisionList})
def updataNews(request):
    newsList = models.News.objects.all()
    listLength = len(newsList)
    flag = 0
    if(listLength >= 3):
        flag = 1
    return render_to_response('updataNews.html',
                              {"listLength":listLength,"newsList":newsList,"flag":flag})    
def createNews(request):
    newsList = models.News.objects.all()
    listLength = len(newsList)
    return render_to_response('createNews.html',{"inputInfo":1})
def deleteNews(request,newsTitle):
    tempNews = models.News.objects.get(Title = newsTitle)
    tempNews.delete()
    newsList = models.News.objects.all()
    listLength = len(newsList)
    flag = 0
    if(listLength >= 3):
        flag = 1
    return render_to_response('updataNews.html',
                              {"listLength":listLength,"newsList":newsList,"flag":flag}) 
def saveNews(request):
    errors = []
    if request.POST:
        tempTitle = request.POST["newsTitle"]
        tempContent = request.POST["newsContent"]
        tempAuthor = request.POST["newsAuthor"]
        tempDate = request.POST["newsData"]
        newsList = models.News.objects.filter(Title = tempTitle)
        #return HttpResponse(tempAuthor)
        if(not(tempTitle) or not(tempContent) or not(tempAuthor) or not(tempDate)):
            errors.append("something is empty!")
            return render_to_response("createNews.html",
                                      {"errors":errors,"inputInfo":1})
        elif(len(newsList)>0):
            errors.append("The title is already exist!")
            return render_to_response("createNews.html",
                                      {"errors":errors,"inputInfo":1})
        else:
            tempNews = models.News()
            tempNews.Title = tempTitle
            tempNews.Text = tempContent
            tempNews.author = tempAuthor
            tempNews.Data = tempDate
            if request.FILES:
                tempNews.Image = request.FILES['newsPicture']
            else:
                tempNews.Image = None
            tempNews.save()
            #upload_to='photos'
            #image = 'photos/%s' % request.FILES['image']
            #upload_to='photos/%Y/%m/%d'
            #now = time.strftime('%Y/%m/%d',time.localtime(time.time()))
            #tempNews.Image = 'photos/%s/%s' %(now,request.FILES["newsPicture"])
            #tempNews.save()
            
            #�涨ͼƬ�Ĵ�С 
            """
            reqfile = request.FILES['newsPicture']
            tempNews.image = Image.open(reqfile)
            tempNews.image.thumbnail((500,500),Image.ANTIALIAS)
            tempNews.image.save("D:/self1/1.jpeg","jpeg")
            #return HttpResponse("success")"""
            return render_to_response("createNews.html",{"createSuccess":1})
def showNews(request,newsTitle):
    news = models.News.objects.get(Title = newsTitle)
    return render_to_response("showNews.html",{"news":news})

def updataIllnessInfo(request):
    allIllnessList = models.Illness.objects.all()
    allDivisionList = models.Division.objects.all()
    return render_to_response("updataIllnessInfo.html",
                             {"allIllnessList":allIllnessList,"allDivisionList":allDivisionList})
def illnessDetailInfomation(request,illnessName):
    allowAddDoctor = []
    illness = models.Illness.objects.get(name = illnessName)
    division = illness.division
    alreadyAddedDoctor = illness.doctor.all()
    allDoctorInDivision = division.doctor_set.all()
    for i in range(0,len(allDoctorInDivision)):
        if(allDoctorInDivision[i] in alreadyAddedDoctor):   #���ڸü����µ�ҽ��
            continue
        else:
            allowAddDoctor.append(allDoctorInDivision[i])   #����������ڸü����µ�ҽ��
    return render_to_response("updataIllnessContent.html",
                              {"alreadyAddedDoctor":alreadyAddedDoctor,
                               "illness":illness,
                               "allowAddDoctor":allowAddDoctor,
                               "division":division,
                               "allowLen":len(allowAddDoctor),
                               "alreadyLen":len(alreadyAddedDoctor)})
 
def updataIllnessSuccess(request):
    if request.POST:
        tempDoctorList = request.POST.getlist("doctorName")
        tempIllnessName = request.POST["illnessdName"]
        illness = models.Illness.objects.get(name =tempIllnessName)#�ҵ�����
        allDivisionList = models.Division.objects.all()#�ҵ����п���
        if(len(tempDoctorList) == 0):
            illness.description = request.POST["illnessDescription"]
            illness.save()
            return render_to_response("updataIllnessInfo.html",
                                      {"allDivisionList":allDivisionList,
                                       "updataSuccess":1})
        else:
            for i in range(0,len(tempDoctorList)):
                tempDoctor = models.Doctor.objects.get(userName = tempDoctorList[0])
                illness.doctor.add(tempDoctor)
            illness.description = request.POST["illnessDescription"]
            illness.save()
            return render_to_response("updataIllnessInfo.html",
                                      {"allDivisionList":allDivisionList,
                                       "updataSuccess":1,
                                       "illnessName":illness.name})
                
    
    
def deleteIllness(request,illnessName):
    tempIllness = models.Illness.objects.get(name = illnessName)
    tempIllness.delete()
    allIllnessList = models.Illness.objects.all()
    allDivisionList = models.Division.objects.all()
    return render_to_response("updataIllnessInfo.html",
                              {"allIllnessList":allIllnessList,"allDivisionList":allDivisionList,"deleteSuccess":1})
                              
def updataIllnessByDivision(request):
    errors = []
    allDivisionList = models.Division.objects.all()
    if request.POST:
        tempDivision = request.POST["divisionType"]
        if(tempDivision == "00000"):
            errors.append("input was nothing!")
            return render_to_response("updataIllnessInfo.html",{"errors1":errors,"allDivisionList":allDivisionList})
        else:
            tempDivision = models.Division.objects.get(divisionID = tempDivision)
            illnessList = tempDivision.illness_set.all()
            return render_to_response("updataIllnessInfo.html",
                                      {"demandByDivision":1,"illnessList":illnessList,"divisionName":tempDivision.name,"allDivisionList":allDivisionList})


def updataIllnessByName(request):
    errors = []
    allDivisionList = models.Division.objects.all()
    if request.POST:
        tempName = request.POST["IllnessName"]
        if not(tempName):
            errors.append("input was nothing!")
            return render_to_response("updataIllnessInfo.html",{"errors0":errors,"allDivisionList":allDivisionList})
        IllnessList = models.Illness.objects.filter(name = tempName)
        if(len(IllnessList)==0):
            errors.append("The Illness wasn't exist!")
            return render_to_response("updataIllnessInfo.html",{"errors0":errors,"allDivisionList":allDivisionList})
        else:
            return render_to_response("updataIllnessInfo.html",
                                      {"demandByIllness":1,"Illness":IllnessList[0],"allDivisionList":allDivisionList})
        
   
    
def addIllnessSuccess(request):
    if request.POST:
        tempName = request.POST["illnessName"]
        tempDivision = request.POST["divisionType"]
        tempDoctorList = request.POST.getlist("doctorName")
        #return HttpResponse(len(tempDoctorList))
        tempIllness = models.Illness.objects.get(name = tempName)
        allDivisionList = models.Division.objects.all()
        for i in range(0,len(tempDoctorList)):
            tempDoctor = models.Doctor.objects.get(userName = tempDoctorList[i])
            tempIllness.doctor.add(tempDoctor)
        return render_to_response("addIllness.html",{"addSuccess":1,"divisionList":allDivisionList})

def illnessAddDoctor(request):
    errors = []
    if request.POST:
        tempName = request.POST["illnessName"]
        tempDivision = request.POST["divisionType"]
        tempDescription = request.POST["illnessDescription"]
        
        allDivisionList = models.Division.objects.all()
        if(not(tempName) or tempDivision == "00000"):
            errors.append("input was nothing!")
            return render_to_response("addIllness.html",
                                      {"errors":errors,"divisionList":allDivisionList})
        
        tempIllness = models.Illness.objects.filter(name = tempName)
        if(len(tempIllness) > 0):   #�жϸü����Ƿ������
            errors.append("the illness is already exist!")
            return render_to_response("addIllness.html",
                                      {"errors":errors,"divisionList":allDivisionList})
        
        tempDivision = models.Division.objects.get(divisionID = tempDivision)
        doctorList = tempDivision.doctor_set.all()
        illness = models.Illness()
        illness.name = tempName
        illness.division = tempDivision
        illness.description = tempDescription
        illness.save()
        #return HttpResponse(doctorList[1].name)
        return render_to_response("addIllness.html",
               {"flag":1,"illnessName":tempName,"divisionName":tempDivision,"doctorList":doctorList})
               
def showDivision(request):
    divisionList = models.Division.objects.all()
    #return HttpResponse(divisionList[1].divisionID)
    return render_to_response("manageDivision.html",{"divisionList":divisionList})  
def deleteDivision(request,divisionID_a):
    divisionTemp = models.Division.objects.get(divisionID = divisionID_a)
    divisionTemp.delete()
    divisionList = models.Division.objects.all()
    #return HttpResponse(divisionList[1].divisionID)
    return render_to_response("manageDivision.html",{"divisionList":divisionList}) 
    
def addDivision(request):
    errors = []
    if request.POST:
        tempID = request.POST["divisionID"]
        tempName = request.POST["name"]
        if(not(tempID) or not(tempName)):
            errors.append("input was nothing!")
            return render_to_response("manageDivision.html",{"errors":errors})
        IDList = models.Division.objects.filter(divisionID = tempID)
        nameList = models.Division.objects.filter(name = tempName)
        if(len(IDList) > 0 or len(nameList) > 0):
            errors.append("The division already exist!")
            return render_to_response("manageDivision.html",{"errors":errors})
        else:
            division = models.Division()
            division.name = request.POST["name"]
            division.divisionID = request.POST["divisionID"]
            division.save()
            return render_to_response("manageDivision.html") 
            
    
    
def deleteAppointDoctor(request,doctorUserName):
    deleteFlag = [1]    
    patient = models.Patient.objects.get(userName = loginPatient.userName)
    doctor = models.Doctor.objects.get(userName = doctorUserName)
    patient.doctorsList.remove(doctor)
    
    #patient = models.Patient.objects.get(userName = loginPatient.userName)
    doctorList = patient.doctorsList.all()
    return render_to_response('appointManage.html',
                              {'deleteFlag':deleteFlag,'doctorList':doctorList,'logins':loginPatient.userName})

def order(request,doctoruserName):
    global loginPatient
    if request.POST:
        date = request.POST['divisionType']
        print 2222
        print date
    doctor = models.Doctor.objects.get(userName = doctoruserName)
    if(loginPatient.userName == 'login'):
           return render_to_response('serviceAppoint.html',
                        {'doctorInformation':doctor, 'nologin':1,
                        'login':loginPatient.userName})
                        
    else:
        
        patient = models.Patient.objects.get(userName = loginPatient.userName)
        
#        book = person.book_set.all()
#        b = models.appointTable.objects.get(appintDate=date)  
#        b.authors.all()  
#        b.authors.filter(first_name='Adam') 
        
        if(int(doctor.appointedPerson[int(date)-1]) == doctor.appointNum):
            return render_to_response('serviceAppoint.html',
                                      {'doctorInformation':doctor,'orderFail':1,
                    'login':loginPatient.userName,'remind':"no doctor"})
      
   #     if(patient.appointeddoctor[t] == 2):
    #        return render_to_response('serviceAppoint.html',
     #                                 {'doctorInformation':doctor,'orderFail':1,
      #              'logins':loginPatient.userName,'remind':"������Ļ���ԤԼ��������������ԤԼ����ʱ��"})
                
        
        
        tables1 = patient.patient_set.all()
        tables2 = models.appointTable.objects.filter(weekNumber = date)
        tables = list(set(tables1) & set(tables2))
        if(tables):
            doctorsOrdered = tables[0].doctorList.all()
            if(doctor in doctorsOrdered):#�鿴��ҽ���Ƿ��Ѿ���ԤԼ
                return render_to_response('serviceAppoint.html',
                                          {'doctorInformation':doctor,'orderFail':1,
                        'login':loginPatient.userName, 'remind':"yibeyuyue"})
                    
            else:
                #doctor = models.Doctor.objects.get(userName = doctoruserName)
                tables[0].doctorList.add(doctor)
                tag= str(int(doctor.appointedPerson[int(date)-1]) + 1)
                doctor.appointedPerson = doctor.appointedPerson[0:(int(date)-1)] + tag + doctor.appointedPerson[int(date):]
  #              patient.appointeddoctor[int(date)] = patient.appointeddoctor[int(date)] + 1
                return render_to_response('serviceAppoint.html',
                                     {'doctorInformation':doctor, 'ordered':1,
                                     'login':loginPatient.userName}) 
        
        else:
#            table = models.appointTable(patient = patient )
            table = models.appointTable()
            table.patient = patient
            table.save()
            table.doctorList.add(doctor)
            table.weekNumber = date
            table.save()
            tag= str(int(doctor.appointedPerson[int(date)-1]) + 1)
            doctor.appointedPerson = doctor.appointedPerson[0:(int(date)-1)] + tag + doctor.appointedPerson[int(date):]
 #           patient.appointeddoctor[int(date)] = patient.appointeddoctor[int(date)] + 1
            return render_to_response('serviceAppoint.html',
                                     {'doctorInformation':doctor, 'ordered':1,
                                     'login':loginPatient.userName}) 

                                      

def demandByDoctor(request):
    global loginPatient
    errors = []
    if request.POST:
        doctorName = request.POST['doctorName']
        if not doctorName:
            #errors.append("Please enter the doctor's name!")
            return render_to_response('mainInterface.html',{'errors1':1,'loginPatient':loginPatient.userName})
        else:
            doctorList = models.Doctor.objects.filter(name = doctorName)
            if(len(doctorList) > 0):
                return render_to_response('serviceAppoint.html',
                        {'doctorName':doctorName,'doctorList':doctorList,'loginPatient':loginPatient.userName})
            else:
                return render_to_response('serviceAppoint.html',{'doctorName':doctorName,'errors':1,'loginPatient':loginPatient.userName})
def demandAllDoctor(request):
    global loginPatient
    doctorList = models.Doctor.objects.all()
    return render_to_response('serviceAppoint.html',
                        {'doctorList':doctorList,'loginPatient':loginPatient.userName})
def detailInformation(reqeust,doctorUserName):
    global loginPatient
    doctorInformation = models.Doctor.objects.get(userName = doctorUserName)
    return render_to_response('serviceAppoint.html',
                              {'doctorInformation':doctorInformation,
                              'logins':loginPatient.userName,"datelist":datesorts})

def demandByDivision(request):
    global loginPatient
    errors = []
    if request.POST:
        divisionIDTemp = request.POST['divisionType']
        if(divisionIDTemp == "00000"):
            divisionList = models.Division.objects.all()
            return render_to_response('mainInterface.html',
                   {"divisionList":divisionList,'errors2':1,'loginPatient':loginPatient.userName})
        else:
            divisionTemp = models.Division.objects.get(divisionID = divisionIDTemp)
            doctorList = divisionTemp.doctor_set.all()
            return render_to_response('serviceAppoint.html',
                    {'divisionName':divisionTemp.name,'doctorList':doctorList,'loginPatient':loginPatient.userName})
            
def demandByIllness(request):
    errors = []
    if request.POST:
        illnessName = request.POST["illnessName"]
        illnessList = models.Illness.objects.filter(name__contains = illnessName)
        if(not illnessName):
            return render_to_response("patient.html",{"noEnter":1})
        elif(len(illnessList) == 0):
            return render_to_response("patient.html",{"noIllness":1})
        else:
            illness = illnessList[0]
            doctorList = illness.doctor.all()
            return render_to_response('serviceAppoint.html',
                                      {"doctorList":doctorList,"illnessName":illness.name})

def patientHome(request):
    if loginPatient.userName == "login":
        divisionList = models.Division.objects.all()
        return render_to_response("mainInterface.html",
                                  {"noLogin":1,"divisionList":divisionList})
    else:
        patient = models.Patient.objects.get(userName = loginPatient.userName)
        return render_to_response("patientHome.html",{"patient":patient})
def RegisterServiceInterface(request):
    global loginPatient
    if loginPatient.userName == "login":
        divisionList = models.Division.objects.all()
        return render_to_response('mainInterface.html',
                                  {'login': loginPatient.userName,"divisionList":divisionList})
    else:
        allDivisionList = models.Division.objects.all()
        return render_to_response('patient.html',
                                  {'login': loginPatient,"allDivisionList":allDivisionList})

def appointManageIntereface(request):
    global loginPatient
    if loginPatient.userName == "login":
        divisionList = models.Division.objects.all()
        return render_to_response('mainInterface.html',
                                  {'login': loginPatient.userName,"divisionList":divisionList})
    else:
        allDivisionList = models.Division.objects.all()
        return render_to_response('appointManage.html',
                                  {'login': loginPatient.userName,"allDivisionList":allDivisionList})

def aboutIntereface(request):
    global loginPatient
    return render_to_response("about.html",{"login":loginPatient})                             

def doctorHome(request,doctorUsername):
    global loginDoctor
    global weekday
    workday = []
    noWorkday = []
    
    doctor = models.Doctor.objects.get(userName = doctorUsername)
    division = doctor.division
    for i in range(0,len(doctor.workTime)):
        if doctor.workTime[i] == "1":
            workday.append(weekday[i+1])
        else:
            noWorkday.append(weekday[i+1])
    #return HttpResponse(len(workday))
    return render_to_response("doctorHome.html",
                              {"workday":workday,"noWorkday":noWorkday,
                              "loginDoctor":loginDoctor,"doctor":doctor,
                              "division":division})

def changeSelfInfo(reqeust):
    flag = 0
    global loginDoctor
    doctor = models.Doctor.objects.get(userName = loginDoctor.userName)
    division = doctor.division
    allDivisionList = models.Division.objects.all()
    if(not doctor.sex):
        flag = 1

    workday = []
    noWorkday = []
    for i in range(0,len(doctor.workTime)):
        if doctor.workTime[i] == "1":
            workday.append(weekday[i+1])
        else:
            noWorkday.append(weekday[i+1])
    return render_to_response("DoctorChangeInfo.html",
                             {"loginDoctor":loginDoctor,"doctor":doctor,"flag":flag,
                              "division":division,"allDivisionList":allDivisionList,
                              "workday":workday,"noWorkday":noWorkday}) 

def updataDoctorInfoSuccess(request):
    global loginDoctor
    global weekdayRever
    global weekday
    if request.POST:
        doctor = models.Doctor.objects.get(userName = request.POST["doctorUserName"])
        nameTemp = request.POST["doctorName"]
                
        if (not nameTemp):
            return render_to_response("doctorChangeInfo.html",{"noName":1})
        else:
            doctor.name = nameTemp
        
        ageTemp = request.POST["doctorAge"]
        if(ageTemp):
            doctor.age = int(ageTemp)
        if(not ageTemp):
            doctor.age = None
        
        if "doctorSex" in request.POST:
            doctor.sex = request.POST["doctorSex"]
        
        doctor.phoneNumber = request.POST["doctorPhone"]
        
        doctor.intro = request.POST["doctorIntro"]
        
        divisionIDTemp = request.POST["doctorDivision"] #������Ŀ���
        divisionTemp = doctor.division                  #ҽ��ԭ�����ڵĿ���
        if(divisionIDTemp == divisionTemp.divisionID):
            doctor.division = doctor.division
        else:
            divisionTemp1 = models.Division.objects.get(divisionID = divisionIDTemp) #�ҵ���ѡ�¿���
            doctor.division = divisionTemp1 #Ϊҽ�����¿���
            illnessList = doctor.illness_set.all()#��ø�ҽ�����µ����м���
            if len(illnessList) == 0:
                noIllness = 1   #����
            else:
                for i in range(0,len(illnessList)):
                    illnessList[i].doctor.remove(doctor)    #Ϊ��ҽ�������м���ɾ����ҽ��
        
        doctor.workTime = "0000000"
        
        workday = request.POST.getlist("doctorWorkTime")
        for i in range(0,len(workday)):
            temp = workday[i]
            index = weekdayRever[temp]-1
            temp1 = doctor.workTime[0:index] + "1" + doctor.workTime[(index+1):7]
            doctor.workTime = temp1
          
        noWorkday = request.POST.getlist("doctorNoWorkTime")
        for i in range(0,len(noWorkday)):
            temp = noWorkday[i]
            index = weekdayRever[temp]-1
            temp1 = doctor.workTime[0:index] + "1" + doctor.workTime[(index+1):7]
            doctor.workTime = temp1
        
        #return HttpResponse(doctor.workTime)
        upperNum= request.POST["personUpper"]
        if(not upperNum):
            return render_to_response("doctorChangeInfo.html",{"noUpperNum":1})
        else:
            doctor.appointNum = int(upperNum)       #������Ϣ������
        
        doctor.save()
        
        doctor = models.Doctor.objects.get(userName = request.POST["doctorUserName"])
        workday = []                                #��ʾ���º����Ϣ
        noWorkday = []
        division = doctor.division
        for i in range(0,len(doctor.workTime)):
            if doctor.workTime[i] == "1":
                workday.append(weekday[i+1])
            else:
                noWorkday.append(weekday[i+1])
        #return HttpResponse(len(noWorkday))
        return render_to_response("doctorHome.html",
                              {"workday":workday,"noWorkday":noWorkday,
                              "loginDoctor":loginDoctor,"doctor":doctor,
                              "division":division,"changeSuccess":1})

def DoctorchangePassword(request):
    global loginDoctor
    doctor = models.Doctor.objects.get(userName = loginDoctor.userName)
    return render_to_response("DchangePassword.html",
                              {"loginDoctor":loginDoctor,"doctor":doctor})      
def DchangePasswordSuccess(request):
    global loginDoctor      
    errors = []
    if request.POST:
        password = request.POST['newPassword']
        confirmPassword = request.POST['confirmPassword']
        doctorUserName = request.POST['doctorUserName']
        doctor = models.Doctor.objects.get(userName = doctorUserName)
        if(confirmPassword != password):
            errors.append("The confirm password isn't correct!")
        elif((not confirmPassword) or (not password)):
            errors.append("Please enter password and confirm password!")
        else:
            doctor.Password = password
            doctor.save()
            return render_to_response("DchangePassword.html",
                              {"loginDoctor":loginDoctor,"doctor":doctor,"changeSuccess":1})   
        return render_to_response("DchangePassword.html",
                              {"loginDoctor":loginDoctor,"doctor":doctor,"errors":errors})    
        
def loginVerify(request):
    errors = []
    divisionList = models.Division.objects.all()
    if request.POST:
        q = request.POST['userName']
        temp = request.POST['Password']
        temp1 = request.POST['confirmPassword']
        if(request.POST['serviceType'] == "3" or not(request.POST['serviceType'])):
            errors.append("please enter user type!")
            return render_to_response('login.html',{'errors':errors})
        elif(request.POST['serviceType'] == "2"):
            author = models.Patient.objects.filter(userName = q)
            if not q:
                errors.append("User name can't be empty!")
            elif(len(author) > 0):
                errors.append("The user already exists!")
            elif(temp != temp1):
                errors.append("Confirm password isn't correct")
            else:
                patient = models.Patient()
                patient.userName = request.POST['userName']
                patient.Password = request.POST['Password']
                patient.userCategory = request.POST["serviceType"]
                patient.save()
                string = "Registered successfully!"
                return render_to_response('mainInterface.html',
                                          {'string':string,'user':patient,
                                          "divisionList":divisionList})
        elif(request.POST['serviceType'] == "1"):
            author = models.Doctor.objects.filter(userName = q)
            if not q:
                errors.append("User name can't be empty!")
            elif(len(author) > 0):
                errors.append("The user already exists!")
            elif(temp != temp1):
                errors.append("Confirm password isn't correct")
            elif(request.POST["divisionType"] == "00000"):
                errors.append("please input the division!")
            else:
                doctor = models.Doctor()
                doctor.userName = request.POST['userName']
                doctor.Password = request.POST['Password']
                doctor.userCategory = request.POST["serviceType"]
                tempDivision = models.Division.objects.get(divisionID = request.POST["divisionType"])
                doctor.division = tempDivision
                doctor.workTime = "0000000"
                doctor.appointedPerson = "0000000"                
                doctor.save()
                string = "Registered successfully!"
                return render_to_response('mainInterface.html',
                                          {'string':string,'user':doctor,
                                           "divisionList":divisionList})
        return render_to_response('login.html',{'errors':errors,"allDivisionList":allDivisionList})

def exitApp(request):
    global loginPatient
    loginPatient.userName = "login"
    divisionList = models.Division.objects.all()
    return render_to_response('mainInterface.html',{'login': loginPatient.userName,
                                                    "divisionList":divisionList})
       
def register(request):
    global loginPatient,URL
    flag0 = 0
    flag1 = 0
    errors = []
    if (request.POST):
        tempName = request.POST['userName']
        tempPassword = request.POST['Password']
        tempCategory = request.POST['serviceType']
        if not tempName:
            errors.append("The user name can't be empty!")
            #return render_to_response('mainInterface.html',{'errors':errors}) 
        else:
            if(tempCategory == '2'):
                try:        
                    user = models.Patient.objects.get(userName = tempName)
                    if(user.Password == tempPassword):
                        loginPatient = user
                        allDivisionList = models.Division.objects.all()
                        return render_to_response("patient.html",
                                                  {'login':loginPatient,"allDivisionList":allDivisionList,
                                                  "URL":URL})
                    else:
                        errors.append("The user name or password is not correct!")
                except models.Patient.DoesNotExist:
                    errors.append("The user name or password is not correct!")
                #return render_to_response('mainInterface.html',{'errors':errors})
            if(tempCategory == '1'):
                try:        
                    user = models.Doctor.objects.get(userName = tempName)
                    if(user.Password == tempPassword):
                        global loginDoctor
                        loginDoctor = user
                        if user.workTime == "0000000":
                                flag0 = 1
                        
                        if((not user.name)or(not user.sex)or(not user.sex)or(not user.sex)
                            or(not user.sex)or(not user.phoneNumber)or(not user.intro)
                            or flag0 == 0 or (not user.appointNum)):
                            fillInfo = 1
                        
                        return render_to_response("DoctorInterface.html",
                                                  {"User":user,"loginDoctor":loginDoctor.userName,
                                                  "fillInfo":fillInfo})
                    else:
                        errors.append("The user name or password is not correct!")
                except models.Doctor.DoesNotExist:
                    errors.append("The user name or password is not correct!")
                #return render_to_response('mainInterface.html',{'errors':errors})
            if(tempCategory == '0'):
                try:        
                    user = models.Administrator.objects.get(userName = tempName)
                    if(user.Password == tempPassword):
                        return render_to_response("administrator.html",{"User":user})
                    else:
                        errors.append("The user name or password is not correct!")
                except models.Administrator.DoesNotExist:
                    errors.append("The user name or password is not correct!")
        return render_to_response('mainInterface.html',{'errors':errors})
    divisionList = models.Division.objects.all()
    return render_to_response('mainInterface.html',
                              {'login': loginPatient.userName,"divisionList":divisionList})         
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    