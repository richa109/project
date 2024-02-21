from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserRegistrationForm 
#import settings.py
from django.conf import settings
#send_mail is built-in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class UserRegisterView(CreateView):
    template_name = 'user/user_register.html'
    model = User
    form_class = UserRegistrationForm
    success_url = '/user/login/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
            


"""class DeveloperRegisterView(CreateView):
    template_name = 'user/developer_register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/user/login/'    """



def sendMail(to):
    subject = 'Welcome to EXPENSE'
    message = 'Hope you are enjoying our website'
   
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    
    return True
    
class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_user:
                return '/user/user_dashboard/'
           
            
def logout_view(request):
    logout(request)
    return redirect('/user/login/')
            
class UserDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/user_dashboard.html')
    
    
    template_name = 'user/user_dashboard.html'

"""class DeveloperDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/developer_dashboard.html')
    
    template_name = 'user/developer_dashboard.html'"""    
       