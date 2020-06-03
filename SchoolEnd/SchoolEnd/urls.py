"""SchoolEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SchoolEnd.view.views import Index,Login,Registered,Registered,UserAdmin,MyWorks,UploadWorks
from SchoolEnd.view.views import worksInfo,topLogin,downLoad,ChangePwd,Admin,adminPage
from SchoolEnd.view.views import UserManage,WorksManage,deleteUser,changeUser,selectUser
from SchoolEnd.view.views import adduser,deleteWorks,selectWorks,changeWorks
urlpatterns = [
    path('xiaoxiong/', Index.as_view(),name='index'),
    path('registered/',Registered.as_view(),name='registered'),
    path('login/',Login.as_view(),name='login'),
    path('userAdmin/',UserAdmin.as_view(),name='userAdmin'),
    path('myWorks/',MyWorks.as_view(),name='myWorks'),
    path("uploadWorks/",UploadWorks.as_view(),name="uploadWorks"),
    path("worksInfo/<int:id>/",worksInfo),
    path("topLogin/",topLogin),
    path("webData/<int:userId>/works/<str:worksId>",downLoad),
    path("changePwd/",ChangePwd.as_view(),name="changePwd"),
    path("admin/",Admin.as_view(),name="admin"),
    path("adminPage/",adminPage),
    path("userManage/",UserManage.as_view(),name="userManage"),
    path("worksManage/",WorksManage.as_view(),name="worksManage"),
    path("deleteUser/<int:id>/",deleteUser),
    path("changeUser/<int:id>/",changeUser),
    path("selectUser/<int:id>/<str:name>/<str:password>/",selectUser),
    path("addUser/",adduser),
    path("deleteWorks/<int:id>/",deleteWorks),
    path("selectWorks/<int:id>/<str:title>/<int:userId>/",selectWorks),
    path("changeWorks/<int:id>/",changeWorks)
]
