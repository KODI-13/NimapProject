from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from myapp.models import Client, User

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def projects(request,id):
    data=Client.objects.get(id=id)
    context={
        'id':id,
        'data':data
    }
    return render(request,'myapp/projects.html',context)  

def registration(request,id):
    data=Client.objects.get(id=id)
    # projects = data.project_set.all()
    context={
        'id':id,
        'data':data,
        # 'projects': projects
    }
    if request.method == 'POST':
        comp=request.POST.get('company')
        pro=request.POST.get('project')
        at=request.POST.get('time')
        by=request.POST.get('cname')
        assign=request.POST.get('user')
        st=request.POST.get('result')
        up=request.POST.get('update')
        data = Client(client_name=comp,project_name=pro,created_at=at,created_by=by,assigned_user=assign,status=st,updated_at=up)
        data.save()
    return render(request,'myapp/registration.html',context)

def display(request):
    data=Client.objects.all()
    data1=User.objects.all()
    context={
        'data':data,
        'data1':data1
    }

    return render(request,'myapp/display.html',context)

def update(request,id):
    data=Client.objects.get(id=id)
    data1=User.objects.all()
    context={
        'data':data,
        'data1':data1
    }
    if request.method == 'POST':
        comp=request.POST.get('company')
        pro=request.POST.get('project')
        by=request.POST.get('cname')
        assign=request.POST.get('user')
        st=request.POST.get('result')
        up=request.POST.get('update')
        data.client_name=comp
        data.project_name=pro
        data.created_by=by
        data.assigned_user=assign
        data.status=st
        data.updated_at=up
        data.save()
        return redirect('/display/')
    return render(request,'myapp/update.html',context)

def cupdate(request,id):
    data1=Client.objects.get(id=id)
    context={
        'id':id,
        'data':data1,
    }
    if request.method == 'POST':
        comp=request.POST.get('company')
        pro=request.POST.get('project')
        at=request.POST.get('time')
        by=request.POST.get('cname')
        data1.client_name=comp
        data1.project_name=pro
        data1.created_at=at
        data1.created_by=by
        data1.save()
    return render(request,'myapp/cupdate.html',context)

def delete(request,id):
    data=Client.objects.get(id=id)
    data.delete()
    return redirect('/display/')
    
def clogin(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')  # Assuming username is passed via GET request
        user=Client.objects.all()
        for i in user:
                if i.uniqueid == input_username:
                    # data = Client.objects.get(id=i.id)
                    # context={
                    #     'data':data
                    # }
                    return redirect('/projects/{}/'.format(i.id),{'id':i.id}) # Redirect to the dashboard page upon successful login
                else:
                    continue
    return render(request,'myapp/clogin.html')

def new(request):
    if request.method == 'POST':
        cn = request.POST.get('clientName')
        un = request.POST.get('username')
        ps = request.POST.get('password')
        data = Client(client_name=cn,uniqueid=un,password=ps)
        data.save()
        return redirect('/clogin/')

    return render(request,'myapp/new.html')