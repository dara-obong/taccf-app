from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class MemberRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = [
            'age',
            'gender',
            'state_of_origin',
            'address',
            'phone_no',
            'office',
            'qualification',
            'status',
            'state_code',
            'ppa',
        ]




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'age',
            'gender',
            'state_of_origin',
            'address',
            'phone_no',
            'office',
            'qualification',
            'status',
            'state_code',
            'ppa',
            'image'
        ]

        def __str__(self):
            return self.get_name_display()