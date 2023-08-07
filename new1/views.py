from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import User1,View1
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404


from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def cp(request):
    if request.method=='POST':
        username=request.user
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        student_id=request.POST.get('student_id')
        phone=request.POST.get('phone')
        branch=request.POST.get('branch')
        year=request.POST.get('year')
        building_name=request.POST.get('building_name')
        room_number=request.POST.get('room_number')
        room_type=request.POST.get('room_type')
        space=request.POST.get('space')
        rent=request.POST.get('rent')
        images1=request.FILES.get('images1')
        
        
       
        
        comments=request.POST.get('comments')
        new_user=User1(username=username,firstname=firstname,lastname=lastname,student_id=student_id,phone=phone,branch=branch,year=year,building_name=building_name,room_number=room_number,room_type=room_type,space=space,rent=rent,images1=images1,comments=comments)
        new_user.username=username
        
        

        
        
        new_user.save()
        
        

        flat6=User1.objects.all()
        context={
            'flat6':flat6
        }
        
        return render(request,'addpostme.html',{'flat6':flat6})



    return render(request,'cp.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        

        user=authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request,user)
            return redirect('all_flat')
        else:
            return render(request,'logincorr.html')
    return render(request,'login.html')

def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
       
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
       
        
        if password!=confirm_password:
            return HttpResponse("password and confirm password are different")
        elif password==confirm_password:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            
            return render(request,'login1.html')
    elif request.method=='GET':
        return render(request,'signup.html')
    else:
        return HttpResponse('An exception occured!Try again')
        

    return render(request,'signup.html')
def all_flat(request):
    flats=User1.objects.all()
    
    context={
        'flats':flats
    }
    
    print(context)
    return render(request,'new_home1.html',{ 'flats':flats})
    


def contact(request,id):
    flats1=User1.objects.get(id=id)
    context={
        'flats1':flats1
    }
    gg=request.user
    
    rr=View1.objects.filter(rentp=gg).first()
    if(rr==None):
        return render(request,'contact.html',{'flats1':flats1})
    else:
        return render(request,'contact2.html',{'flats1':flats1})
    

def newhomepage(request):
    return render(request,'new_home.html')

def newhomepage1(request):
    return render(request,'new_home1.html')

def post(request):
    user22=request.user
    
    flats2=User1.objects.filter(username=user22)
    
    context={
        'flats2':flats2
    }
    return render(request,'flat_user.html',{'flats2':flats2})


def userlogout(request):
    logout(request)
    request.session.clear()
    return redirect('loginpage')

def post1(request):
    flat3=User1.objects.all()
    context={
        'flat3':flat3
    }
    return render(request,'post1.html',{'flat3':flat3})


def useredit1(request,id):
    flat4=User1.objects.get(id=id)
    context={
        'flat4':flat4
    }
    return render(request,"userflat.html",{'flat4':flat4})


def delpost1(request,id):
    y=User1.objects.get(id=id)
    y.delete()
    flat5=User1.objects.all()
    context={
        'flat5':flat5
    }
    return render(request,'delpostme.html',{'flat5':flat5})

def view11(request,id):
    owner=request.user
    
    interested1=User1.objects.get(id=id)
    context={
        'interested1':interested1
    }
    yy=interested1.username
    flat11=id
    if request.method=='POST':
        ownername=request.POST.get('ownername')
        branch=request.POST.get('branch')
        year=request.POST.get('year')
        phone=request.POST.get('phone')
    newuser=View1(rentp=owner,owner=yy,flatid=flat11,ownername=ownername,branch=branch,year=year,phone=phone)
    if(owner!=yy):
        newuser.save()
    return render(request,'contact1.html',{'interested1':interested1})

def notify1(request):
    rr=request.user
    zz=View1.objects.filter(rentp=rr).first()
    if(zz==None):
        return HttpResponse("No Notification")
    else:
        zz1=View1.objects.filter(rentp=rr)
        context={
            'zz1':zz1
        }
        zz2=zz1.rentp
        print(f"owner is",zz2)
        dd1=User.objects.filter(username=zz2).first()
        print(f"dd1",dd1)

        dd3=User1.objects.filter(username=dd1).count()
        print(dd3)
        if dd3>1:
            dd2=User1.objects.filter(username=dd1)
            context={
                'dd2':dd2
           }
        
            return render(request,'notify11.html',{'dd2':dd2})
        else:
            dd2=User1.objects.filter(username=dd1)
            context={
                'dd2':dd2
           }
        
            return render(request,'notify11.html',{'dd2':dd2})
        

def loginpage1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        

        user=authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request,user)
            return redirect('all_flat')
        else:
            return render(request,'logincorr.html')
    return render(request,'login1.html')


    


   














