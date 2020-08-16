from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Employee, HrCompany



# Create your views here.
@login_required
def dashboard(request):
    employee = Employee.objects.all()
    hr_company = HrCompany.objects.all()
    
    context = {'employees': employee, 
                'hr_company': hr_company} # once the hr user log in, the hr user 
                                    # will be able to see the employees on the DB
    return render( request, 'user_hr/dashboard.html', context) 



def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "GET":
        
        context = { 'form' : UserRegistrationForm }
        
        return render(request, "registration/register.html", context)
    
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save() #save/create user in the database
            user = form.cleaned_data.get('username')
            
            messages.success(request, f'Account created for {user}!')
                                    # if user was created successfully then,
            return redirect('login')    # take client to the loginpage
