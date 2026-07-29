from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationFrom, VerityCodeForm, UserloginForm
from utils import send_otp_code
import random
from .models import otpcodes
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

class UserRegisterView(View):
    form_class = UserRegistrationFrom
    template_name = 'account/register.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            otpcodes.objects.create(phone_number = form.cleaned_data['phone'], code = random_code)
            request.session['user_registration_info'] = {
                'phone_number' : form.cleaned_data['phone'],
                'email : ' : form.cleaned_data['email'],
                'full_name' : form.cleaned_data['full_name'],
                'password' : form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you an activation code' , 'success')
            return redirect('account:verify_code')
        return render (request,self.template_name, {'form':form})

class UserVerifyRegisterCodeView(View):
    form_class = VerityCodeForm
    def get(self, request):
        form = self.form_class
        return render(request, 'account/verify.html', {'form':form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = otpcodes.objects.get(phone_number = user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd ['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['full_name'], user_session['password'])
                code_instance.delete()

                messages.success(request, 'You have successfully verified your account' , 'success')
            else:
                messages.error(request, 'The code you entered is invalid' , 'error')
                return redirect('account:verify_code')
            return redirect('home:home')

class UserLoginView(View):
    form_class = UserloginForm
    def get(self, request):
        form =self.form_class()
        return render(request, 'account/login.html', {'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone_number = cd['phone_number']
            password = cd['password']
            user = authenticate(phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in' , 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'Invalid phone number or password' , 'error')
                return redirect('home:home')















# Create your views here.
