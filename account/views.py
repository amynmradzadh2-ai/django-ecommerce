from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationFrom, VerityCodeForm, UserloginForm
from utils import send_email_code
import random
from .models import EmailOTP, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.Cart import Cart

class UserRegisterView(View):
    form_class = UserRegistrationFrom
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(100000, 999999)
            send_email_code(form.cleaned_data['email'], random_code)
            EmailOTP.objects.create(email=form.cleaned_data['email'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you an activation code', 'success')
            return redirect('account:verify_code')
        return render(request, self.template_name, {'form': form})


class UserVerifyRegisterCodeView(View):
    form_class = VerityCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = EmailOTP.objects.get(email=user_session['email'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(
                    user_session['phone_number'],
                    user_session['email'],
                    user_session['full_name'],
                    user_session['password']
                )
                code_instance.delete()
                messages.success(request, 'You have successfully verified your account', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'The code you entered is invalid', 'error')
                return redirect('account:verify_code')
        return render(request, 'account/verify.html', {'form': form})


class UserLoginView(View):
    form_class = UserloginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'Invalid phone number or password', 'error')
                return redirect('home:home')
        return render(request, 'account/login.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out', 'success')
        return redirect('home:home')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'account/profile.html', {
            'profile_user': request.user,
            'cart_items_count': len(cart),
        })