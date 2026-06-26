from django.shortcuts import render,redirect

# Create your views here.

from .models import *
from app.models import *

# opt generator from the render method
from  random import randint


def IndexPage(request):
    return render(request,"app/index.html")


def SingupPage(request):
    return render(request,"app/signup.html")



# register Candidate and Company

def RegisterUser(request):

    if request.method == "POST":

        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # Check Email Exists
        if UserMaster.objects.filter(email=email).exists():

            return render(request, "app/signup.html", {
                'msg': 'User Already Exists'
            })

        # Check Password Match
        if password != cpassword:

            return render(request, "app/signup.html", {
                'msg': 'Password and Confirm Password Do Not Match'
            })

        otp = randint(100000, 999999)

        # Create User
        newuser = UserMaster.objects.create(
            role=role,
            email=email,
            password=password,
            otp=otp
        )

        # Candidate Registration
        if role == "Candidate":

            Candidate.objects.create(
                user_id=newuser,
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname')
            )

        # Company Registration
        elif role == "Company":

            Company.objects.create(
                user_id=newuser,
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname'),
                company=request.POST.get('company')
            )

        return render(request, "app/otpverify.html", {
            'email': email
        })

    return render(request, "app/signup.html")

# Otp page
def OTPpage(request):
    return render(request,"app/otpverify.html")

# Otp page Verifie both

def Otpverify(request):
    email=request.POST['email']
    otp=int(request.POST['otp'])
    user=UserMaster.objects.get(email=email)
    if user:
        if user.otp==otp:
            message="OTP Verify SuccsessFully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message="OTP is Inccorect"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        return render(request,"app/signup.html",)
    
def Loginpage(request):
    return render(request,'app/login.html')

# Login Candidate and Company

def LoginUser(request):

    if request.method == "POST":

        role = request.POST.get('role', '').strip().lower()
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("Form Role :", role)
        print("Email :", email)

        try:
            user = UserMaster.objects.get(email=email)
            print("DB Role :", user.role)

        except UserMaster.DoesNotExist:

            return render(request, "app/login.html", {
                'msg': 'User Does Not Exist'
            })

        # Password Check
        if user.password != password:

            return render(request, "app/login.html", {
                'msg': 'Incorrect Password'
            })

        db_role = user.role.strip().lower()

        print("DB Role After Lower :", db_role)

        # Candidate Login
        if role == "candidate" and db_role == "candidate":

            try:

                can = Candidate.objects.get(user_id=user)

                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email

                print("Candidate Login Success")

                return redirect('index')

            except Candidate.DoesNotExist:

                return render(request, "app/login.html", {
                    'msg': 'Candidate Profile Not Found'
                })

        # Company Login
        elif role == "company" and db_role == "company":

            print("Company Block Entered")

            try:

                com = Company.objects.get(user_id=user)

                print("Company Found :", com.company)

                request.session['id'] = user.id
                request.session['role'] = user.role.lower()
                request.session['firstname'] = com.firstname
                request.session['lastname'] = com.lastname
                request.session['company'] = com.company
                request.session['email'] = user.email

                print("Redirecting To Company Index")

                return redirect('companyindex')

            except Company.DoesNotExist:

                print("Company Profile Not Found")

                return render(request, "app/login.html", {
                    'msg': 'Company Profile Not Found'
                })

        else:

            print("Invalid Role Selected")

            return render(request, "app/login.html", {
                'msg': 'Invalid Role Selected'
            })

    return render(request, "app/login.html")


#  profile page

def ProfilePage(request,pk):

    user=UserMaster.objects.get(pk=pk)
    can=Candidate.objects.get(user_id=user)
    return render(request, "app/profile.html",{'user':user,'can':can})

# Update Candidate Datas

def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)

    if user.role == 'Candidate':
        can = Candidate.objects.get(user_id=user)

        if request.method == "POST":

            can.contact = request.POST.get('contact')
            can.city = request.POST.get('city')
            can.state = request.POST.get('state')
            can.address = request.POST.get('address')
            can.dob = request.POST.get('dob')
            can.gender = request.POST.get('gender')

            can.country = request.POST.get('country')
            can.website = request.POST.get('website')

            can.job_type = request.POST.get('job_type')
            can.job_catagry = request.POST.get('job_catagry')
            can.job_description = request.POST.get('job_description')

            # Salary fields
            can.min_salary = request.POST.get('min_salary')
            can.max_salary = request.POST.get('max_salary')

            if 'profile_pic' in request.FILES:
                can.profile_pic = request.FILES['profile_pic']

            can.save()

        return redirect(f'/profile/{pk}')
    

# logout Page

def Logout(request):
    
    request.session.flush()

    return redirect('register')


# apply pages Admin 


def ApplyPage(request, job_id):
    if 'id' not in request.session:
        return redirect('loginpage')

    user = UserMaster.objects.get(id=request.session['id'])
    can = Candidate.objects.get(user_id=user)
    job = JobDetails.objects.get(id=job_id)

    if request.method == "POST":

        ApplyList.objects.create(
            candidate=can,
            job=job,

            firstname=request.POST.get('firstname', ''),
            lastname=request.POST.get('lastname', ''),

            jobname=request.POST.get('jobname', ''),

            city=request.POST.get('city', ''),
            state=request.POST.get('state', ''),
            country=request.POST.get('country', ''),
            address=request.POST.get('address', ''),

            dob=request.POST.get('dob', ''),

            education=request.POST.get('education', ''),

            website=request.POST.get('website', ''),

            email=request.POST.get('email', ''),

            contact=request.POST.get('contact', ''),

            min_salary=request.POST.get('min_salary', ''),
            max_salary=request.POST.get('max_salary', ''),

            gender=request.POST.get('gender', ''),

            resume=request.FILES.get('resume')
        )

        return redirect('joblist')


    return render(request, "app/company/apply.html", {
        "user": user,
        "can": can,
        "job": job,
    })




##################Company Side##################

def CompanyIndexPage(request):
    return render(request,'app/company/index.html')




def CompanyProfilePage(request):

    # Login check
    if 'id' not in request.session:
        return redirect('login')

    # Role check
    if request.session.get('role', '').lower() != 'company':
        return redirect('index')

    company = Company.objects.get(
        user_id=request.session['id']
    )

    if request.method == "POST":

        company.firstname = request.POST.get('firstname')
        company.lastname = request.POST.get('lastname')
        company.company = request.POST.get('company')
        company.contact = request.POST.get('contact')
        company.state = request.POST.get('state')
        company.city = request.POST.get('city')
        company.address = request.POST.get('address')
        company.description = request.POST.get('description')

        if 'logo_pic' in request.FILES:
            company.logo_pic = request.FILES['logo_pic']

        company.save()

    return render(
        request,
        "app/company/register.html",
        {"company": company}
    )

def CompanyLogout(request):

    request.session.flush()

    return redirect('login')





def JobDetailsSubmit(request):

    if 'id' not in request.session:
        print("SESSION ID NAHI HAI")
        return redirect('loginpage')

    try:
        user = UserMaster.objects.get(id=request.session['id'])
        print("USER MILA:", user.email, "ROLE:", user.role)
    except UserMaster.DoesNotExist:
        print("USER DATABASE MEIN NAHI HAI")
        request.session.flush()
        return redirect('loginpage')

    if request.method == "POST":
        print("POST REQUEST AAYA")
        if user.role.lower() == "company":
            print("COMPANY ROLE SAHI HAI")
            try:
                company = Company.objects.get(user_id=user)
                print("COMPANY MILI:", company.company)
                JobDetails.objects.create(
                    company_id=company,
                    jobname=request.POST.get('jobname'),
                    companyname=request.POST.get('companyname'),
                    companyaddress=request.POST.get('companyaddress'),
                    jobdescription=request.POST.get('jobdescription'),
                    qualification=request.POST.get('qualification'),
                    resposibilities=request.POST.get('resposibilities'),
                    location=request.POST.get('location'),
                    companywebsite=request.POST.get('companywebsite'),
                    companyemail=request.POST.get('companyemail'),
                    companycontact=request.POST.get('companycontact'),
                    salarypackeg=request.POST.get('salarypackeg'),
                    companyimage=request.FILES.get('companyimage'),
                    expreience=request.POST.get('expreience'),
                )
                print("JOB SAVE HO GAYI")
                return redirect('jobpostlist')
            except Exception as e:
                print("ERROR:", e)
    else:
        print("GET REQUEST HAI - FORM DIKHAO")

    return render(request, "app/company/jobpost.html")




def JobPostPage(request):

    if 'id' not in request.session:
        return redirect('loginpage')

    all_job = JobDetails.objects.all()

    print("Total Jobs =", all_job.count())

    return render(
        request,
        "app/company/jobpostlist.html",
        {"all_job": all_job}
    )









def CandidateJobListPost(request):

    all_job=JobDetails.objects.all()

    return render(request, "app/job-list.html",{"all_job": all_job})



# ###################### ADMIN Site##################
def AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def AdminIndexPage(request):

    if 'username' in request.session and 'password' in request.session:

        username = request.session['username']

        return render(request, "app/admin/index.html", {
            "username": username
        })

    else:
        return redirect('adminloginpage')

def AdminLogin(request):
    username=request.POST['username']
    password=request.POST['password']

    if username=="admin" and password=="admin":
         request.session['username']=username
         request.session['password']=password
         return redirect('adminindex')
    else:
        message="username and password does not match"
        return render(request,"app/admin/login.html",{"msg":message})
    
def AdminUserList(request):
    if 'username' not in request.session:
        return redirect('adminloginpage')
    all_user=UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{"alluser":all_user})


def AdminComapnyList(request):
    if 'username' not in request.session:
        return redirect('adminloginpage')
    all_company=UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{"allcompany":all_company})

def VerifyCompany(request, pk):
    if 'username' not in request.session:
        return redirect('adminloginpage')
    user = UserMaster.objects.get(pk=pk)
    user.is_verified = True
    user.save()
    return redirect('companylist')


def UserDelete(request,pk):
    user=UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')
def CompanyDelete(request,pk):
    company=UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')




def Contact(request):
    return render(request,'app/contact.html')

def Service(request):
    return render(request,'app/services.html')

def About(request):
    return render(request,'app/about.html')
