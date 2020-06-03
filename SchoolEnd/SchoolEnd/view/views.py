from django.views.generic.base import View
from django.http import HttpResponse,Http404,FileResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
import json
import pymysql
import random
import os
conn = pymysql.connect(host="localhost",
                               user="root",
                               database="SchoolEnd",
                               charset="utf8",
                               passwd="Leigel_123"
                               )
cursor = conn.cursor()
def adminlogin(request):
    if("id" in request.COOKIES):
        userId = request.COOKIES['id']
        password = request.COOKIES['password']
        sql = "select * from admin where userId=" + userId + " and password= \"" + password + "\""
        print(sql)
        cursor.execute(sql)
        selectData = cursor.fetchall()
        if (len(selectData) == 1):
            return {'username': selectData[0][2], 'userId': selectData[0][0]}
        else:
            return 0;
    else:
        return 0;

def userlogin(request):
    if("id" in request.COOKIES):
        userId=request.COOKIES['id']
        password=request.COOKIES['password']
        sql = "select * from user where Id=" + userId + " and password= \"" + password + "\""
        print(sql)
        cursor.execute(sql)
        selectData = cursor.fetchall()
        if(len(selectData)==1):
            return {'username':selectData[0][2],'userId':selectData[0][0]}
        else:
            return 0;
    else:
        return 0;
class Index(View):
    def __init__(self):
        pass
    def get(self,request):
        sql="select worksId,worksTitle,worksInformation from works"
        cursor.execute(sql)
        data={"data":cursor.fetchall()}
        datakey=("worksId","title","content")
        newdata=[]
        for worksdata in data['data']:
            newdata.append(dict(zip(datakey,worksdata)))
        print(newdata)
        data["data"]=newdata
        sql = "select worksId,worksTitle,worksInformation from works"
        cursor.execute(sql)
        viewContent = cursor.fetchall()
        if ("id" not in request.COOKIES or "password" not in request.COOKIES):
            reResponse = render(request, 'first.html',data)
            return reResponse
        else:
            userId = request.COOKIES['id']
            password = request.COOKIES.get('password')
            print(password)
            sql = "select * from user where Id=" + userId + " and password= \"" + password + "\""
            print(sql)
            cursor.execute(sql)
            selectData = cursor.fetchall()
            print(selectData)
            if (len(selectData) == 0):
                reResponse=render(request, 'first.html',data)
                return reResponse
            elif (len(selectData) == 1):
                data['username']=selectData[0][2]
                print(data['username'])
                print("37")
                reResponse=render(request, 'first.html',data)
                reResponse.set_cookie("id", userId)
                reResponse.set_cookie("password", password)
                return reResponse
    def post(self,request):
            pass
class Login(View):
    def __init__(self):
        pass
    def get(self,request):
        global conn
        global cursor
        if (request.method == 'GET'):
            return render(request, "login.html")
    def post(self,request):
        global conn
        global cursor
        PostData = json.loads(request.body)
        sql = "select * from user where Id="
        sql+=PostData["Id"] + " and password= \"" + PostData["password"] + "\""
        cursor.execute(sql)
        selectData = cursor.fetchall()
        if (len(selectData) == 0):
            return HttpResponse(0)
        elif (len(selectData) == 1):
            httpresponse = HttpResponse(1)
            if("id" in request.COOKIES):
                httpresponse.delete_cookie("id")
            if("password" in request.COOKIES):
                httpresponse.delete_cookie("password")
            httpresponse.set_cookie('id', PostData['Id'],path="/",secure=False,max_age=86400*7)
            httpresponse.set_cookie('password', PostData['password'],secure=False,path="/",max_age=86400*7)
            print(PostData['password'])
            return httpresponse
        else:
            return HttpResponse(2)

class Registered(View):
    global conn
    global cursor
    def __init__(self):
        pass
    def get(self,request):
        return render(request,"registered.html")
    def post(self,request):
        postData=json.loads(request.body)
        userId=int(random.random()*1000)
        sql="select * from user where id="+str(userId)
        cursor.execute(sql)
        a = cursor.fetchall()
        while(len(a)!=0):
            userId=int(random.random()*1000)
            sql="select * from user where id="+str(userId)
            print(sql)
            a=cusor.execute(sql)
        sql="insert into user(Id,name,password) value("
        sql+=str(userId)+",\""+postData['name']+"\",\""+postData['password']+"\")"
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return HttpResponse(userId)
class UserAdmin(View):
    def __init__(self):
        pass
    def get(self,request):
        name=userlogin(request)
        if(name!=0):
            return render(request,"userAdmin.html",name)
        response=render(request,"userAdmin.html")
        return response
class MyWorks(View):
    def __init__(self):
        pass
    def get(self,request):
        user=userlogin(request)
        if(user!=0):
            sql="select worksId,worksTitle from works where authorId="+str(user['userId'])
            print(sql)
            cursor.execute(sql)
            sqlData=cursor.fetchall()
            if (len(sqlData)!=0):
                key=["id","title"]
                works=[]
                for i in sqlData:
                    works.append(dict(zip(key,i)))
                data={}
                data['data']=works
                return render(request,'myWork.html',data)
            else:
                return render(request,"error.html")
        else:
            return render(request,"pleaseLogin.html")
class UploadWorks(View):
    def __init__(self):
        pass
    def get(self,request):
        name = userlogin(request)
        if (name != 0):
            return render(request, "uploadWoks.html", name)
        return render(request,'pleaseLogin.html')
    def post(self,request):
        name = userlogin(request)
        if(len(request.FILES)==2 and request.POST['title']!=None and request.POST['content']!=None):
            if (name != 0):
                worksId=int(random.random()*1000)
                sql="select* from works where worksId="+str(worksId)
                cursor.execute(sql)
                selectData = cursor.fetchall()
                while(len(selectData)!=0):
                    worksId=int(random.random()*1000)
                    sql = "select* from works where worksId=" + str(worksId)
                    cursor.execute(sql)
                    selectData = cursor.fetchall()
                os.chdir("/home/leigel/SchoolEnd/static/webData")
                if(not os.path.exists(str(name['userId']))):
                    os.mkdir(str(name['userId']))
                os.chdir(str(name["userId"]))
                if(not os.path.exists("video")):
                    os.mkdir("video")
                if(not os.path.exists("works")):
                    os.mkdir("works")
                works=request.FILES['works']
                video=request.FILES["video"]
                videoName=video.name
                worksName=works.name
                worksPath="/home/leigel/SchoolEnd/static/webData/"+str(name["userId"])+"/works"
                videoPath="/home/leigel/SchoolEnd/static/webData/"+ str(name["userId"]) +"/video"
                os.chdir(worksPath)
                worksfile=open(str(worksId)+worksName,"wb+")
                for chunk in works.chunks():
                    worksfile.write(chunk)
                os.chdir(videoPath)
                videofile=open(str(worksId)+videoName,"wb+")
                for chunk in video.chunks():
                    videofile.write(chunk)
                authorId=request.COOKIES["id"]
                worksTitle=request.POST['title']
                worksInformation=request.POST["content"]
                worksPath="/static/webData/"+str(name["userId"])+"/works/"+str(worksId)+worksName
                videoPath="/static/webData/"+str(name["userId"])+"/video/"+str(worksId)+videoName
                sql='''insert into works(worksId,worksTitle,worksInformation,
                worksVideoPath,worksPath,authorId) value('''+str(worksId)+''',\"'''+worksTitle+'''\",
                \"'''+worksInformation+'''\",\"'''+videoPath+'''\",\"'''+worksPath+'''\",'''+authorId+''')'''
                cursor.execute(sql)
                conn.commit()
                worksfile.close()
                video.close()
                return redirect("/myWorks/")
        else:
            return HttpResponse("请正确上传")



def worksInfo(request,id):
    if(request.method=="GET"):
        sql="select worksTitle,worksInformation,worksVideoPath,worksPath from works"
        sql+=" where worksId="+str(id)
        cursor.execute(sql)
        nowdata=cursor.fetchall()
        key=["title","worksInfo","videoPath","worksPath"]
        data=dict(zip(key,nowdata[0]))
        return render(request,"worksInfo.html",data)
def topLogin(request):
    if(request.method=="GET"):
        a=userlogin(request)
        print(a)
        return HttpResponse(a['username'])

def downLoad(request,userId,worksId):
    path=request.path
    worksPath="/home/leigel/SchoolEnd"+path
    works=open(worksPath,"rb")
    response=FileResponse(works)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="example.tar.gz"'
    works.close()
    return response

class ChangePwd(View):
    def __init__(self):
        pass
    def get(self,request):
        userInf=userlogin(request)
        if (userInf!=0):
            return render(request,"changePwd.html")
    def post(self,request):
        userInf=userlogin(request)
        if(userInf!=0):
            postData = json.loads(request.body)
            sql = "update user set name=\""
            sql += postData['name'] + "\",password=\"" + postData['password'] + "\" "
            sql+="where id="+str(request.COOKIES['id'])
            print(sql)
            cursor.execute(sql)
            conn.commit()
            nowData=HttpResponse(0)
            nowData.delete_cookie("password")
            nowData.set_cookie('password', postData['password'],secure=False,path="/",max_age=86400*7)
            return HttpResponse(0)

class Admin(View):
    def __init__(self):
        pass
    def get(self,request):
        return render(request,"adminLogin.html")
    def post(self,request):
        global conn
        global cursor
        PostData = json.loads(request.body)
        sql = "select * from admin where userId="
        sql += PostData["Id"] + " and password= \"" + PostData["password"] + "\""
        cursor.execute(sql)
        selectData = cursor.fetchall()
        if (len(selectData) == 0):
            return HttpResponse(0)
        elif (len(selectData) == 1):
            httpresponse = HttpResponse(1)
            httpresponse.set_cookie('id', PostData['Id'], path="/", secure=False, max_age=86400 * 7)
            httpresponse.set_cookie('password', PostData['password'], secure=False, path="/", max_age=86400 * 7)
            print(PostData['password'])
            return httpresponse;
        else:
            return HttpResponse(2)

def adminPage(request):
    if(request.method=="GET"):
        return render(request,"admin.html")

class UserManage(View):
    def __init__(self):
        pass
    def get(self,request):
        if(adminlogin(request)!=0):
            sql="select * from user"
            cursor.execute(sql)
            nowdata=cursor.fetchall()
            key=["Id","password","name"]
            data=[]
            for i in nowdata:
                data.append(dict(zip(key,i)))
            model={}
            model['data']=data
            return render(request,"userManage.html",model)
    def post(self,request):
        pass

class WorksManage(View):
    def __init__(self):
        pass
    def get(self,request):
        sql="select worksId,worksTitle,authorId from works"
        cursor.execute(sql)
        worksData=cursor.fetchall()
        keys=["Id","title","author"]
        data=[]
        for i in worksData:
            data.append(dict(zip(keys,i)))
        return render(request,"worksManage.html",{"data":data})
    def post(self,request):
        pass

def selectUser(request,id,name,password):
    if (request.method=="GET"):
        if(id==0 and name=="none" and password=="none"):
            sql = "select * from user"
            cursor.execute(sql)
            nowdata = cursor.fetchall()
            key = ["Id", "password", "name"]
            data = []
            for i in nowdata:
                data.append(dict(zip(key, i)))
            model = {}
            model['data'] = data
            return render(request, "userManage.html", model)
        else:
            data={}
            if(id==0):
                pass
            else:
                data['id']=id
            if(name=="none"):
                pass
            else:
                data["name"]=name
            if(password=="none"):
                pass
            else:
                data["password"]=password
            i=0
            keys=list(data.keys())
            sql="select * from user where "
            while(i<(len(data.keys())-1)):
                if(type(data.get(keys[i])) is int):
                    sql+=keys[i]+"="+str(data.get(keys[i]))+" and "
                if(type(data.get(keys[i])) is str):
                    sql+=keys[i]+"=\""+data.get(keys[i])+"\" and "
                i+=1
            if (type(data.get(keys[i])) is int):
                sql += keys[i] + "=" + str(data.get(keys[i]))
            if (type(data.get(keys[i])) is str):
                sql += keys[i] + "=\"" + data.get(keys[i]) + "\""
            cursor.execute(sql)
            nowdata=cursor.fetchall()
            key = ["Id", "password", "name"]
            data = []
            for i in nowdata:
                data.append(dict(zip(key, i)))
            model = {}
            model['data'] = data
            return render(request, "userManage.html", model)
    else:
        return Http404
def deleteUser(request,id):
    if(adminlogin(request)!=0):
        os.chdir("/home/leigel/SchoolEnd/static/webData/")
        os.system("rm -rf "+ str(id))
        sql="delete from works where authorId="+str(id)
        cursor.execute(sql)
        conn.commit()
        sql="delete from user where Id="+str(id)
        cursor.execute(sql)
        conn.commit()
        return HttpResponse(1)
def changeUser(request,id):
    if (adminlogin(request) != 0):
        if (request.method=="GET"):
            sql="select * from user where Id="+str(id)
            cursor.execute(sql)
            userData=cursor.fetchall()
            data={}
            key=["id","password","name"]
            data["data"]=dict(zip(key,userData[0]))
            return render(request,"adminChangeUser.html",data)
        if(request.method=="POST"):
            PostData = json.loads(request.body)
            sql="select * from user where id="+str(id)
            cursor.execute(sql)
            nowdata=cursor.fetchall()
            print(PostData["id"]==str(id))
            if(len(nowdata)==0 or str(id)==PostData["id"]):
                userid=PostData["id"]
                password=PostData["password"]
                name=PostData["name"]
                sql="update user set name="+str(userid)+",password=\""+password+"\",name=\""+name+"\""
                sql+=" where Id="+str(id)
                print(sql)
                cursor.execute(sql)
                conn.commit()
                return HttpResponse(1)
            else:
                return HttpResponse(0)
def adduser(request):
    if(request.method=="GET"):
        return render(request,"adduser.html")

def deleteWorks(request,id):
    sql="select worksVideoPath,worksPath from works where worksId="+str(id)
    print(sql)
    cursor.execute(sql)
    path=cursor.fetchall()
    print(path)
    key=["video","works"]
    nowpath=dict(zip(key,path[0]))
    allPath=("/home/leigel/SchoolEnd")
    com=allPath+nowpath["video"]
    os.system("rm -rf "+com)
    com=allPath+nowpath["works"]
    os.system("rm -rf "+com)
    sql="delete from works where worksId="+str(id)
    cursor.execute(sql)
    conn.commit()
    return HttpResponse(1)
def selectWorks(request,id,title,userId):
    if (request.method=="GET"):
        if(id==0 and title=="none" and userId==0):
            sql = "select worksId,worksTitle,authorId from works"
            cursor.execute(sql)
            worksData = cursor.fetchall()
            keys = ["Id", "title", "author"]
            data = []
            for i in worksData:
                data.append(dict(zip(keys, i)))
            return render(request, "worksManage.html", {"data": data})
        else:
            data={}
            if(id==0):
                pass
            else:
                data['worksId']=id
            if(title=="none"):
                pass
            else:
                data["worksTitle"]=title
            if(userId==0):
                pass
            else:
                data["authorId"]=userId
            i=0
            keys=list(data.keys())
            sql="select worksId,worksTitle,authorId from works where "
            while(i<(len(data.keys())-1)):
                if(type(data.get(keys[i])) is int):
                    sql+=keys[i]+"="+str(data.get(keys[i]))+" and "
                if(type(data.get(keys[i])) is str):
                    sql+=keys[i]+"=\""+data.get(keys[i])+"\" and "
                i+=1
            if (type(data.get(keys[i])) is int):
                sql += keys[i] + "=" + str(data.get(keys[i]))
            if (type(data.get(keys[i])) is str):
                sql += keys[i] + "=\"" + data.get(keys[i]) + "\""
            print(sql)
            cursor.execute(sql)
            worksData=cursor.fetchall()
            keys = ["Id", "title", "author"]
            data = []
            for i in worksData:
                data.append(dict(zip(keys, i)))
            return render(request, "worksManage.html", {"data": data})
    else:
        return Http404

def changeWorks(request,id):
    if(request.method=="GET"):
        sql="select worksTitle,worksInformation from works where worksId="+str(id)
        cursor.execute(sql)
        sqldata=cursor.fetchall()
        key=["title","content"]
        data={}
        data["works"]=dict(zip(key,sqldata[0]))
        return render(request,"changeWorks.html",data)
    elif(request.method=="POST"):
        postData = json.loads(request.body)
        sql="update works set worksTitle= \""+postData["title"]
        sql+="\",worksInformation=\""+postData["worksContent"]
        sql+="\" where worksId="+str(id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        return HttpResponse(0)
    else:
        return Http404