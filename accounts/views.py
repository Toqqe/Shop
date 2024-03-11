from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView

from . import forms
from accounts.models import Profile, Address
# Create your views here.

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = forms.LoginForm
    next_page = '/'

class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    

class RegisterView(View):
    def get(self,request):
        form = forms.RegisterForm()

        return render(request, "accounts/register.html", {
            "form": form
        })

    def post(self,request):
        form = forms.RegisterForm(request.POST)
        username = form['username']

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user_login = authenticate(username=username, password=password)
            login(request,user_login)
            
            user_profile = Profile.objects.create(user=request.user)
            user_profile.save()
            
            return HttpResponseRedirect('/')
        else:
            return render(request, "accounts/register.html", {
                "form": form
            })

    
class AccountView(View):
    def get(self, request):
        user_profile = request.user.profile

        # home_address1 = user_profile.address_set.get(type=1)
        home = Address.objects.filter(profile=user_profile, type=1).first()
        home_address = forms.HomeAddressForm(instance=home)

        delivery = Address.objects.filter(profile=user_profile, type=2).first()
        delivery_address = forms.DeliveryAddressForm(instance=delivery)


        initial = {'email': request.user.email}
        user_form = forms.UserProfileUpdateForm(instance=user_profile, initial=initial)

        return render(request, "accounts/account.html", {
            "home_address": home_address,
            "delivery_address": delivery_address,
            "user_form": user_form
        }) 
    
    def post(self, request):
        user_profile = request.user.profile

        home_address = forms.HomeAddressForm(instance=user_profile)
        delivery_address = forms.DeliveryAddressForm(instance=user_profile)

        
        if 'home-address-form' in request.POST:
            home = Address.objects.filter(profile=user_profile, type=1).first()
            form = forms.HomeAddressForm(request.POST, instance=home)

            if form.is_valid():
                address = form.save(commit=False)
                address.profile = user_profile
                address.type = 1
                address.save()
                
                return redirect('account')
            
        if 'delivery-address-form' in request.POST:
            delivery = Address.objects.filter(profile=user_profile, type=2).first()
            form = forms.DeliveryAddressForm(request.POST, instance=delivery)

            if form.is_valid():
                address = form.save(commit=False)
                address.profile = user_profile
                address.type = 2
                address.save()
                
                return redirect('account')

        if 'account-form' in request.POST:
            form = forms.UserProfileUpdateForm(request.POST, instance=user_profile)

            if form.is_valid():
                user = user_profile.user
                user.email = form.cleaned_data['email']
                user.save() ## Saving user email - User
                form.save() ## Saving user data - UserProfile
                return redirect('account')
        else:
            return render(request, "accounts/account.html", {
            "home_address": home_address,
            "delivery_address": delivery_address,
            "user_form": form
            }) 


def accountView(request):
    curr_user = request.user

    context ={
        "curr_user" : curr_user,
    }
    return render(request, "accounts/orders.html",context)






                # if 'checkbox-addres' in request.POST and request.POST['checkbox-addres'] == 'on':
                #     delivery_add = forms.AddressForm(request.POST)

                #     if delivery_add.is_valid():
                #         delivery_add.cleaned_data = form.cleaned_data
                #         delivery_add.type = 2
                #         delivery_add.save()