
from atexit import register
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from.models import *

# Create your views here.
def base(request):
    return render(request,"base.html")
def reg(request):
    return render(request,"reg.html")



def head(request):
    if request.method=='GET':
        return render(request,'headreg.html')
    elif request.method=='POST':
        fn=request.POST["fname1"]
        ln=request.POST["lname"]
        un=request.POST["uname"]
        pswd=request.POST["pswd"]
        gen=request.POST["ge"]
        adr=request.POST["adr"]
        cate=request.POST["cat"]
        place=request.POST["place"]
        city=request.POST["city"]
        pin=request.POST["pin"]
        ph=request.POST["mob"]
        sal=request.POST["salary"]
        em=request.POST["employess"]
        print(fn,ln,un,pswd,gen,adr,place,city,pin)


        reg=Register()
        reg.firstname=fn
        reg.lastname=ln
        reg.username=un
        reg.password=pswd
        reg.gender=gen
        reg.address=adr
        reg.phone=ph
        reg.category=cate
        reg.place=place
        reg.city=city
        reg.pin=pin
        reg.salary=sal
        reg.employess=em
        reg.save()
    return render(request,"login.html")
def user(request):
    if request.method=='GET':
        return render(request,'userreg.html')
    elif request.method=='POST':
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        un=request.POST["uname"]
        pswd=request.POST["pswd"]
        ph=request.POST["mob"]

        use=userform()
        use.firstname=fn
        use.lastname=ln
        use.username=un
        use.password=pswd
        use.phone=ph
        use.save()
    return render(request,"userlogin.html")

def login(request):
     if request.method=='GET':
        return render(request,"login.html")
     else:
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            reg=Register.objects.get(username=username,password=password)
            if reg:
                request.session['userid']=reg.id
                return redirect('headhome')
        except:
            return render(request,"login.html",{'msg':'login failed'})

def userlogin(request):
     if request.method=='GET':
        return render(request,"userlogin.html")
     else:
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            use=userform.objects.get(username=username,password=password)
            if use:
                request.session['userid']=use.id
                return redirect('userhome')
        except:
            return render(request,"userlogin.html",{'msg':'login failed'})
def userview(request):
    if 'userid' in request.session:
        data=userform.objects.all()
        return render(request,"userview.html",{'name':data})
    else:
        return redirect('userhome')
def employeview(request):
        data=employeeform.objects.all()
        return render(request,"employeview.html",{'name':data})
def employeereg(request):
    if request.method=='GET':
        return render(request,'employereg.html')
    elif request.method=='POST':
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        gen=request.POST["ge"]
        ph=request.POST["mob"]
        qual=request.POST["qual"]
        heid=request.POST["hid"]
        cate=request.POST["cat"]

        em=employeeform()
        em.firstname=fn
        em.lastname=ln
        em.gender=gen
        em.phone=ph
        em.qualification=qual
        em.headrid=heid
        em.category=cate
        em.save()
    return render(request,'employereg.html')
def headhome(request):
    return render(request,'headhome.html')

def userhome(request):
    return render(request,'userhome.html')

def headview(request):
    if 'userid' in request.session:
        data=Register.objects.all()
        return render(request,"headview.html",{'name':data})
    else:
        return redirect('userhome')

def reqform(request,id):
    if request.method=='GET':
        salary=Register.objects.get(id=id)
        print(salary)
        return render(request,'requestform.html',{'hid':id,"uid":request.session['userid'],'sal':salary.salary})
    elif request.method=='POST':
        hid=request.POST["hid"]
        uid=request.POST["uid"]
        da=request.POST["date"]
        empl=request.POST["emp"]
        sal=request.POST["sal"]
        
        rf=requestform()
        rf.headerid=hid
        rf.userid=uid
        rf.date=da
        rf.employe=empl
        rf.salary=sal
        
        rf.save()
    return render(request,'requestform.html')

def req(request):
        id = request.session['userid']
        data=requestform.objects.filter(headerid=id)
        print(data)
     
        return render(request,"request.html",{'name':data})


def adlogin(request):
     if request.method=='GET':
        return render(request,"admin.html")
     else:
        username='saron'
        password=1234
        print(username,password)
        return redirect('adminhome')
        
def adminhome(request):
    return render(request,'adminhome.html')


  
    
       

    
        


    

