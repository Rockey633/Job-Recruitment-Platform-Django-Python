from django.urls import path,include

from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SingupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OTPpage,name="otppage"),
    path("otp/",views.Otpverify,name="otp"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("updateprofile/<int:pk>/",views.UpdateProfile,name="updateprofile"),
    path('logout/', views.Logout, name='logout'),


   path('joblist/', views.CandidateJobListPost, name='joblist'),
#    path('apply/', views.ApplyPage, name='apply'),
    path('apply/<int:job_id>/', views.ApplyPage, name='apply'),



    ########### Company Side URLS #################
    path("companyindex/", views.CompanyIndexPage, name="companyindex"),
    path("companyprofile/", views.CompanyProfilePage, name="companyprofile"),
    path("companylogout/", views.CompanyLogout, name="companylogout"),


    path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
    path("jobpost/",views.JobDetailsSubmit,name="jobpost"),
    path("jobpostlist/",views.JobPostPage,name="jobpostlist"),
    path('joblist/', views.CandidateJobListPost, name='joblist'),


    # ###################### ADMIN Site##################
    path('adminloginpage/', views.AdminLoginPage, name='adminloginpage'),
    path('adminindex/', views.AdminIndexPage, name='adminindex'),
    path('adminlogin/', views.AdminLogin, name='adminlogin'),
    
    path('adminuserlist/', views.AdminUserList, name='userlist'),
    path('admincompanylist/', views.AdminComapnyList, name='companylist'),
    path('verifycompany/<int:pk>/', views.VerifyCompany, name='verifycompany'),
    path('deleteuser/<int:pk>/', views.UserDelete, name='deleteuser'),
    path('deletecompany/<int:pk>/', views.CompanyDelete, name='deletecompany'),



    path('contact/', views.Contact, name='contact'),
    path('services/', views.Service, name='services'),
    path('about/', views.About, name='about'),

    
]
