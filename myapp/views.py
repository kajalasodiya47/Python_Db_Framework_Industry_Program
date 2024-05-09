from django.shortcuts import render
from . models import *
import random
from . utils import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

# chairmen and member login logic
def login(request):
    if request.POST:
       try:
         uid = User.objects.get(email=request.POST['email'],password=request.POST['password'])
         if uid:
              print(uid.role)
              if uid.role == "chairman":
                    cid = Chairman.objects.get(userid=uid)
                    #print(cid.userid)
                    request.session['email'] = uid.email
                    #request.session['profile'] = cid.pic.url
                    return render(request,"home.html",{'uid':uid,'cid':cid})
              else:
                    mid = Member.objects.get(userid=uid)
                    request.session['email'] = uid.email
                    #request.session['profile'] = cid.pic.url
                    return render(request,"memberhome.html",{'uid':uid,'mid':mid})
       except:
           msg1 = "Invalid email or password" 
           return render(request,"login.html",{'msg1':msg1}) 
    else:   
        return render(request,"login.html")

# logout functionality
def logout(request):
    if "email" in request.session:
       del request.session['email']
       return render(request,"login.html")  
    else: 
        return render(request,"login.html") 

# chairmen profile logic    
def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid:
           cid = Chairman.objects.get(userid=uid)
           return render(request,"profile.html",{'uid':uid,'cid':cid})  
    else:     
        return render(request,"login.html")

# change password logic for chairman and member   
def change_pass(request):
    if "email" in request.session:
          uid = User.objects.get(email=request.session['email'])    
          if uid.password == request.POST['cpass']:
             uid.password = request.POST['npass']
             uid.save()
             del request.session['email']
             msg = "Successfully Password Changed!!"
             return render(request,"login.html",{'msg':msg})
          else:
              msg1 = "Confirm password does not match"
              del request.session['email']
              return render(request,"login.html",{'msg1':msg1})

# chairmen profile edit logic       
def pedit(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
       cid = Chairman.objects.get(userid = uid)
       print("hello")
       if request.POST:
          print(cid.userid)
          cid.firstname = request.POST['firstname']
          cid.lastname = request.POST['lastname']
          cid.contact = request.POST['contact']
          cid.houseno = request.POST['houseno']
          cid.blockno = request.POST['blockno']
          if "pic" in request.FILES:
              cid.pic = request.FILES['pic']
              cid.save()
          cid.save()
          return render(request,"profile.html",{'uid':uid,'cid':cid})  
       else:
          return render(request,"profile.html",{'uid':uid,'cid':cid}) 

# member profile edit logic 
def mempedit(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
       mid = Member.objects.get(userid = uid)
       print("hello")
       if request.POST:
          print(mid.userid)
          mid.firstname = request.POST['firstname']
          mid.lastname = request.POST['lastname']
          mid.contact = request.POST['contact']
          mid.houseno = request.POST['houseno']
          mid.blockno = request.POST['blockno']
          if "pic" in request.FILES:
              mid.pic = request.FILES['pic']
              mid.save()
          mid.save()
          return render(request,"memberprofile.html",{'uid':uid,'mid':mid})  
       else:
          return render(request,"memberprofile.html",{'uid':uid,'mid':mid})         

# add member logic
@csrf_exempt       
def addMember(request):  
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
       cid = Chairman.objects.get(userid = uid)    
       if request.POST:
          email = request.POST['email']
          firstname = request.POST['firstname']
          l1 = ["2we45","89gd0","9yus4","hf833","n302s"]
          password = random.choice(l1)+email[3:6]
          print(password)
          muid = User.objects.create(email = request.POST['email'],password = password,role = "member")
          if muid:
              mid = Member.objects.create(
                 userid = muid,
                 firstname = request.POST['firstname'],
                 lastname = request.POST['lastname'],
                 contact  = request.POST['contact'], 
                 blockno = request.POST['blockno'],
                 houseno = request.POST['houseno'],   
                 occupation = request.POST['occupation'],
                 job_address = request.POST['jobaddress'],
                 blood_grp = request.POST['bloodgroup'],
                 vehicle_details = request.POST['vehicledetails'],
               ) 
              if mid:
                 # mail functionality 
                 mymailfunction("Welcome to Digital Society","confirmation_mail",email,{'firstname':firstname,'password':password})
              return render(request,"addmember.html",{'uid' : uid,'cid' : cid, 's_msg' : "Successfully Member added!!"})
    return render(request,"addmember.html",{'uid':uid,'cid':cid})

# forget password logic
def forget_pass(request):
    if request.POST:
      email = request.POST['email']
      code = random.randint(100001,999999)
      request.session['code'] = code
      request.session['email'] = email
      mymailfunction("Welcome to Digital Society","mymailtemplate",email,{'email':email,'code':code})
      return render(request,"email_verification_code.html")
    else: 
       return render(request,"forget_pass.html")

# forget password logic for verify otp  
def email_verify(request):    
    if request.POST:
        code = int(request.session['code'])
        ucode = int(request.POST['ucode'])
        if code == ucode:
            del request.session['code']
            return render(request,"new_pass.html")
        else:
            return render(request,"email_verification_code.html")
    else:    
       return render(request,"email_verification_code.html")

# forget password logic for update password     
def new_pass(request):
    if request.POST:
        user = User.objects.get(email=request.session['email']) 
        if request.POST['password'] == request.POST['cpassword']:
            user.password = request.POST['password']  
            user.save()
            return render(request,"login.html")
        else:
            return render(request,"new_pass.html")
    else:
         return render(request,"new_pass.html")   

# all society members view logic
def allSocietymembers(request):   
    uid = User.objects.get(email=request.session['email']) 
    cid = Chairman.objects.get(userid = uid)
    mall = Member.objects.all()
    return render(request,"allsocietymem.html",{'mall':mall,'uid':uid,'cid':cid})       

# member profile
def memberProfile(request): 
    uid = User.objects.get(email=request.session['email']) 
    mid = Member.objects.get(userid=uid)  
    return render(request,"memberprofile.html",{'uid':uid,'mid':mid})  