from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#username: shaw  || password: Bikki084@

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return render(request,'index.html')
    return render(request, 'welcome.html')
   

def store(request):
    return render(request,'store.html')

def about(request):
    return render(request,'about.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')


def loginUser(request):
      if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

      return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'index.html')