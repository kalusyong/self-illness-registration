# -*- coding: gbk -*-
from django.shortcuts import*
from register import models
from django.http import HttpResponse,HttpResponseRedirect
from PIL import Image
import time
# Create your views here.
loginPatient = models.Patient()
loginPatient.userName = 'login'
login = loginPatient
#loginPatient = models.Patient.objects.filter(userName = '登录')

def mainInterface(request):
    global loginPatient
    return render_to_response('mainInterface.html',{'logins': loginPatient.userName })
def loginInterface(request):
    return render_to_response('login.html')
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
            #upload_to='photos'
            #image = 'photos/%s' % request.FILES['image']
            #upload_to='photos/%Y/%m/%d'
            now = time.strftime('%Y/%m/%d',time.localtime(time.time()))
            tempNews.Image = 'photos/%s/%s' %(now,request.FILES["newsPicture"])
            tempNews.save()
            #规定图片的大小 
            """
            reqfile = request.FILES['newsPicture']
            tempNews.image = Image.open(reqfile)
            tempNews.image.thumbnail((500,500),Image.ANTIALIAS)
            tempNews.image.save("D:/self1/1.jpeg","jpeg")
            #return HttpResponse("success")"""
            return render_to_response("createNews.html",{"createSuccess":1})
def showNews(request,newsTitle):
    tempNews = models.News.objects.get(Title = newsTitle)
    return render_to_response("showNews.html",{"news":tempNews})
def registraServiceInterface(request):
    print


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
        if(allDoctorInDivision[i] in alreadyAddedDoctor):   #已在该疾病下的医生
            continue
        else:
            allowAddDoctor.append(allDoctorInDivision[i])   #还可以添加在该疾病下的医生
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
        illness = models.Illness.objects.get(name =tempIllnessName)#找到疾病
        allDivisionList = models.Division.objects.all()#找到所有科室
        if(len(tempDoctorList) == 0):
            illness.description = request.POST["illnessdDescription"]
            illness.save()
            return render_to_response("updataIllnessInfo.html",
                                      {"allDivisionList":allDivisionList,
                                       "updataSuccess":1})
        else:
            for i in range(0,len(tempDoctorList)):
                tempDoctor = models.Doctor.objects.get(userName = tempDoctorList[0])
                illness.doctor.add(tempDoctor)
            illness.description = request.POST["illnessdDescription"]
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
        if(len(tempIllness) > 0):   #判断该疾病是否已添加
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
def appointManageIntereface(request):
    global loginPatient
    patient = models.Patient.objects.get(userName = loginPatient.userName)
    doctorList = patient.doctorsList.all()
    return render_to_response('appointManage.html',
                              {'doctorList':doctorList,'logins':loginPatient.userName})
def order(request,doctoruserName):
    global loginPatient
    
    doctor = models.Doctor.objects.get(userName = doctoruserName)
    if(loginPatient.userName == 'login'):
           return render_to_response('serviceAppoint.html',
                        {'doctorInformation':doctor, 'nologin':1,
                        'logins':loginPatient.userName})
                        
    else:
        patient = models.Patient.objects.get(userName = loginPatient.userName)
        doctorsOrdered = patient.doctorsList.all()
        if(doctor in doctorsOrdered):#查看该医生是否已经被预约
            return render_to_response('serviceAppoint.html',
                                      {'doctorInformation':doctor,'orderFail':1,
                                       'logins':loginPatient.userName})
        else:
            #doctor = models.Doctor.objects.get(userName = doctoruserName)
            patient = models.Patient.objects.get(userName = loginPatient.userName)
            patient.doctorsList.add(doctor)
            return render_to_response('serviceAppoint.html',
                                     {'doctorInformation':doctor, 'ordered':1,
                                     'logins':loginPatient.userName}) 
                                    
def newMassageInterface(request):
    print  
def signOut(request):
    global loginPatient
    loginPatient = login
    return render_to_response('mainInterface.html',{'logins': loginPatient.userName })
def demandDoctor(request):
    global loginPatient
    errors = []
    if request.POST:
        doctorName = request.POST['doctorName']
        if not doctorName:
            errors.append("Please enter the doctor's name!")
            return render_to_response('mainInterface.html',{'errors1':errors})
        else:
            try:
                doctorList = models.Doctor.objects.filter(name = doctorName)
                return render_to_response('serviceAppoint.html',
                        {'doctorName':doctorName,'doctorList':doctorList
                         ,'logins':loginPatient.userName})
            except models.Doctor.DoesNotExist:
                errors.append("The doctor does not exist")
                return render_to_response('serviceAppoint.html',{'errors':errors})
def detailInformation(reqeust,doctorUserName):
    global loginPatient
    doctorInformation = models.Doctor.objects.get(userName = doctorUserName)
    return render_to_response('serviceAppoint.html',
                              {'doctorInformation':doctorInformation,'logins':loginPatient.userName})
def demandDivision(request):
    global loginPatient
    divisions = {'3':'0011','2':'0010','1':'0001','4':'0100'}
    errors = []
    if request.POST:
        divisionNum = request.POST['divisionType']
        divisionIDTemp = divisions[divisionNum]
        try:
            divisionTemp = models.Division.objects.get(divisionID = divisionIDTemp)
            doctorList1 = divisionTemp.doctor_set.all()
            return render_to_response('serviceAppoint.html',
                    {'divisionName':divisionTemp.name,'doctorList1':doctorList1,
                    'logins':loginPatient.userName})
        except models.Doctor.DoesNotExist:
            errors.append("nobody!")
            return render_to_response('serviceAppoint.html',{'errors1':errors})
            
def demandIllness(request):
    errors = []                
    return render_to_response('serviceAppoint.html')
        
def loginVerify(request):
    errors = []
    if request.POST:
        q = request.POST['userName']
        temp = request.POST['Password']
        temp1 = request.POST['confirmPassword']
        if(request.POST['serviceType'] == "2"):
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
                                          {'string':string,'user':patient})
        elif(request.POST['serviceType'] == "1"):
            author = models.Doctor.objects.filter(userName = q)
            if not q:
                errors.append("User name can't be empty!")
            elif(len(author) > 0):
                errors.append("The user already exists!")
            elif(temp != temp1):
                errors.append("Confirm password isn't correct")
            else:
                doctor = models.Doctor()
                doctor.userName = request.POST['userName']
                doctor.Password = request.POST['Password']
                doctor.userCategory = request.POST["serviceType"]
                doctor.save()
                string = "Registered successfully!"
                return render_to_response('mainInterface.html',
                                          {'string':string,'user':doctor})
        return render_to_response('login.html',{'errors':errors})
        
def register(request):
    global loginPatient
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
                        return render_to_response("patient.html",{'logins':loginPatient.userName})
                    else:
                        errors.append("The user name or password is not correct!")
                except models.Patient.DoesNotExist:
                    errors.append("The user name or password is not correct!")
                #return render_to_response('mainInterface.html',{'errors':errors})
            if(tempCategory == '1'):
                try:        
                    user = models.Doctor.objects.get(userName = tempName)
                    if(user.Password == tempPassword):
                        patientList = user.patient_set.all()
                        return render_to_response("doctorOrderedCheck.html",
                                                  {"User":user,'patientList':patientList})
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
            
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    