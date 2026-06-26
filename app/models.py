from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField()
    role=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="app/img/candidate")
    min_salary = models.CharField(max_length=100, default="0")
    max_salary = models.CharField(max_length=100, default="0")
    country=models.CharField(max_length=50, default="")
    website=models.URLField(max_length=150, default="")
    job_type=models.CharField(max_length=50, default="")
    job_catagry=models.CharField(max_length=50, default="")
    job_description=models.TextField( default="")
    profile_pic=models.ImageField(upload_to="app/img/candidate",default="")




class Company(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    company=models.CharField(max_length=150, default="")
    state=models.CharField(max_length=50, default="")
    city=models.CharField(max_length=50, default="")
    contact=models.CharField(max_length=50, default="")
    address=models.CharField(max_length=150, default="")
    description = models.TextField(default="")
    company_web = models.CharField(max_length=250,default="")
    logo_pic=models.ImageField(upload_to="app/img/company", default="")

    

class JobDetails(models.Model):
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE , null=True,blank=True)
    jobname=models.CharField(max_length=250, default="")
    companyname=models.CharField(max_length=250, default="")
    companyaddress=models.CharField(max_length=250, default="")
    jobdescription=models.TextField(max_length=500, default="")
    qualification=models.CharField(max_length=250, default="")
    resposibilities=models.CharField(max_length=250, default="")
    location=models.CharField(max_length=250, default="")
    companywebsite=models.CharField(max_length=250, default="")
    companyemail=models.CharField(max_length=250, default="")
    companycontact=models.CharField(max_length=250, default="")
    salarypackeg=models.CharField(max_length=250, default="")
    companyimage=models.ImageField(upload_to="app/img/jobpost", default="",null=True,
    blank=True)
    expreience=models.IntegerField(null=True, blank=True, default=0)




class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE)

    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")

    jobname = models.CharField(max_length=200, default="")

    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=300, default="")

    dob = models.CharField(max_length=50, default="")

    education = models.CharField(max_length=200, default="")

    website = models.CharField(max_length=200, default="")

    email = models.EmailField(default="")

    contact = models.CharField(max_length=20, default="")

    min_salary = models.CharField(max_length=200, default="")
    max_salary = models.CharField(max_length=200, default="")

    gender = models.CharField(max_length=50, default="")

    resume = models.FileField(upload_to="app/resume/")


    def __str__(self):
        return self.firstname + " " + self.lastname
    



