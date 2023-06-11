import random
from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,"index.html")
def signup(request):
    if request.method == "POST":
        User.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            gender=request.POST['gender'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            city=request.POST['city'],
            address=request.POST['address'],
            password=request.POST['password'],
            profile_pic=request.FILES['profilepic'],
        )
        msg="Your Data Submit Successfully!!"
        return render(request,"signup.html",{'msg':msg})
    else:
        return render(request,"signup.html")

def contact(request):
    if request.method =="POST":
        Contact.objects.create(
            fname=request.POST['fname'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            remarks=request.POST['remarks'],

        )
        msg="your data submitted succeccfully"
        contact=Contact.objects.all().order_by("-id")[:3]
        return render(request,"contact.html",{'msg':msg,'contact':contact})
    else:
        contact=Contact.objects.all().order_by("-id")[:3]
        return render(request,"contact.html",{'contact':contact})
def login(request):
    if request.method == "POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email']=user.email
                request.session['profilepic']=user.profile_pic.url
                request.session['fname']=user.fname
                msg="Login Successfully"
                return render(request,"index.html",{'msg':msg})
            else:
                msg="Your Password Is Incoreect"
                return render(request,"login.html",{'msg':msg})
        except:
            msg="Your Email Is Incorrect"
            return render(request,"login.html",{'msg':msg})

    else:
        return render(request,"login.html")
    
def logout(request):
    try:
        del request.session['email']
        del request.session['profile_pic']
        return render(request,"login.html")
    except:
        return render(request,"login.html")

def changepassword(request):
    if request.method == "POST":
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=User.objects.get(email=request.session['email'])
        if user.password == password:
            msg="Please Dont Use Your Old Password"
            return render(request,"changepassword.html",{'msg':msg})
        else:
            if password == cpassword:
                user.password=password
                user.save()
                msg="Your Password Change Successfully!!"
                del request.session['email']
                return render(request,"login.html",{'msg':msg})
            else:
                msg="Your Password And Confrim Password Does Not Meatch"
                return render(request,"changepassword.html",{'msg':msg})

    else:
        return render(request,"changepassword.html")
    
def forgetpassword(request):
    if request.method == "POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject = 'OTP For Forgote Password'
            message = 'Dear, '+user.fname+" "+user.lname+",\n You have reqquested for a new password.\nOTP: "+str(otp) +"\n Don't Share any one Your OTP and Password \n Thank You"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            msg="Sent OTP"
            return render(request,"otp.html",{'msg':msg,'otp':otp,'email':user.email})
        except:
            msg="Your Email Is Not Register"
            return render(request,"forgetpassword.html",{'msg':msg})

    else:
        return render(request,"forgetpassword.html")
    
def otp(request):
    otp=request.POST['otp']
    uotp=request.POST['uotp']
    email=request.POST['email']
    if otp == uotp:
        return render (request,"newpassword.html",{'email':email})
    else:
        msg="Your OTP Is Inccorrect"
        return render (request,"otp.html",{'msg':msg,'otp':otp,'email':email})
def newpassword(request):
    
    email=request.POST['email']
    password=request.POST['password']
    cpassword=request.POST['cpassword']
    user=User.objects.get(email=email)
    if user.password == password:
        msg="Please Dont Use Your Old Password"
        return render(request,"newpassword.html",{'msg':msg,'email':email})
    else:
        if password == cpassword:
            user.password=password
            user.save()
            msg="Your Password Change Successfully"
            return render(request,"login.html",{'msg':msg})
        else:
            msg="Your Password And Confrim Password Does Not Metch"
            return render(request,"newpassword.html",{'msg':msg,'email':email})

def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method == "POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.gender=request.POST['gender']
        user.mobile=request.POST['mobile']
        user.city=request.POST['city']
        user.address=request.POST['address']
        try:
            user.profile_pic=request.FILES['profilepic']
        except:
            pass
        user.save()
        request.session['profilepic']=user.profile_pic.url

        msg="Your Profile Update Successfully"
        return render(request,"profile.html",{'user':user,'msg':msg})
    else:
        return render(request,"profile.html",{'user':user})
