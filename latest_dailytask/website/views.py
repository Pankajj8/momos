from django.shortcuts import render, redirect
from .models import Project,Task,Message,TaskUpdate,Login
from .forms import FormProject,FormTask,FormTaskUpdate,FormLogin
import  datetime

# Create your views here.

def dashboard(request):
    return render(request,"dashboard.html",None)

def  taskDetail(request):
    id = request.GET.get('id')
    request.session["tid"] = id

    if id is not None:
        row = Task.objects.filter(Tid=id)
        upd1 = TaskUpdate.objects.filter(Tid=id)




    return  render(request,"taskDetail.html",{'row':row,'updates':upd1})


def mytasks(request):
    obj  = Task.objects.all()

    return  render(request,"mytasks.html",{'tasks':obj})

def messages(request):

    msg = request.POST.get('msg')
    sender_uname =1
    rec_uname =2

    if msg is not None:
        new_object = Message(sender_username=sender_uname,receiver_username=rec_uname,content=msg)
        new_object.save()

    obj = Message.objects.all()


    return  render(request,"messages.html",{'msg':obj})





def addProject(request):
    
    PTname =request.POST.get('Pname')
    CTname =request.POST.get('Cname')
    CTdetails=request.POST.get('Cdetails')
    PTdescription =request.POST.get('Pdescription')
    PTdeadline =request.POST.get('Pdeadline')
    PTstartdate =request.POST.get('Pstartdate')
    PTmanagedby =request.POST.get('Pmanagedby')
    PTcontract =request.POST.get('Pcontract')
    PTimage1 =request.FILES.get('Pimage1')
    PTimage2 =request.FILES.get('Pimage2')
    PTimage3 =request.FILES.get('Pimage3')
    PTtextresource =request.POST.get('Ptextresource')

    if PTname is  not None and CTname is  not  None and CTdetails is not None and PTdescription is not None and PTdeadline is not None and PTstartdate is not None and  PTmanagedby is not None and  PTcontract is not None and  PTimage1 is not None and  PTimage2 is not None and  PTimage3 is not None and  PTtextresource is not None:
        new_object =Project(Pstatus=0,Pname=PTname,Cname=CTname,Cdetails=CTdetails,Pdescription=PTdescription,Pdeadline=PTdeadline,Pstartdate=PTstartdate,Pmanagedby=PTmanagedby,Pcontract=PTcontract,Pimage1=PTimage1,Pimage2=PTimage2,Pimage3=PTimage3,Ptextresource=PTtextresource)
        new_object.save()

    fProject = FormProject()
    return render(request,"addProject.html",{'fProject':fProject})

def addTask(request):



    TPid = request.session.get('pid')
    TPtitle = request.POST.get('Ttitle')
    TPstatus = 0
    TPtechnology = request.POST.get('Ttechnology')
    TPassignedto = request.POST.get('Tassignedto')
    TPassignedby = request.POST.get('Tassignedby')
    TPassigndate =   request.POST.get('Tassigneddate')
    TPdealine = request.POST.get('Tdeadline')

    if TPtechnology is  not None and  TPtitle is  not None and TPstatus is  not None and  TPtechnology is  not None and TPassignedto is  not None and TPassignedby is  not None and  TPassigndate is  not None and TPdealine is  not None:

         new_object = Task(Pid=TPid,Ttitle=TPtitle,Tstatus = TPstatus,Ttechnology=TPtechnology,Tassignedto=TPassignedto,Tassignedby=TPassignedby,Tassigneddate=TPassigndate,Tdeadline=TPdealine)
         new_object.save()
         return  redirect('http://localhost:8000/website/projectDetail?id='+request.session.get('pid'))

    fTask=FormTask()
    return  render(request,"addTask.html",{'fTask':fTask})

def homepage(request):
    return render(request,"base.html", None)

def viewallprojects(request):

    obj = Project.objects.all()
    return render(request,"viewallprojects.html", {'project':obj})


def  projectDetail(request):

    id  = request.GET.get('id')
    request.session["pid"] =id

    if id  is  not None:
        row =  Project.objects.filter(Pid=id)
        tasks= Task.objects.filter(Pid=id)

    return  render(request,"projectDetail.html",{'row':row,'tasks':tasks,'Pid':id})


def addTaskUpdate(request):

    mTid = request.session.get('tid')
    mUtitle = request.POST.get('Utitle')
    mUDtime = datetime.datetime.now()
    mUdescription = request.POST.get('Udescription')
    mUempname = request.POST.get('Uempname')
    mUimg1 = request.FILES.get('Uimg1')
    mUimg2 = request.FILES.get('Uimg2')
    mUimg3 = request.FILES.get('Uimg3')

    if mUtitle is not None:
        f = TaskUpdate(Tid=mTid,Utitle=mUtitle,UDtime = mUDtime,Uimg1= mUimg1,Uimg2=mUimg2,Uimg3=mUimg3,Udescription=mUdescription,Uempname=mUempname)
        f.save()

        return redirect("http://localhost:8000/website/taskDetail?id="+request.session.get('tid'))




    formTaskUpdate = FormTaskUpdate()

    return render(request,"addTaskUpdate.html",{'addUpdateForm':formTaskUpdate})


def loginpage(request):

        usrname=request.POST.get("username")
        passwrd=request.POST.get("password")

        if usrname is not None and passwrd is not None:
            row= Login(username=usrname,password=passwrd)
            row.save()

            return redirect("http://localhost:8000/website/loginpage")


        flogin = FormLogin()

        return render(request, "loginpage.html", {'flogin': flogin})




