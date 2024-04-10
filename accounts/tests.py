from django.test import TestCase

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from .models import Profile
from .forms import RegisterForm
# Create your tests here.

class CreateProfile(TestCase):
    def setUp(self):
        # Creating client
        self.client = Client()
        
        # Data
        self.username = "test"
        self.email = "test@test.com"
        self.password = "PassWoRd123!$"
        
    def test_profile_create_with_user(self):
        """
        
        Returs 2x True if Profile instance is created corectly  
        
        """
        ##Form data
        form_data = {
            "username":self.username,
            "email":self.email,
            "password1":self.password,
            "password2":self.password,
        }        
        
        ## Simulate POST request
        client = Client()
        reg_url = reverse('register-page')
        response = client.post(reg_url, data=form_data)
        
        self.assertEqual(response.status_code, 302) ## Redirect(HttpResponseRedirect) after creating user/profile
        
        created_user = User.objects.filter(username=self.username).first()
        created_profile = Profile.objects.filter(user=created_user).first()
        
        self.assertTrue(created_profile) ## Return True if Profile exist(query based on created user)