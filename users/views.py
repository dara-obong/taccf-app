from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import MemberRegisterForm, MemberProfileForm, UserUpdateForm, ProfileUpdateForm
from django.core.exceptions import PermissionDenied


# Create your views here.

def register(request):
    if request.method == 'POST':
        mr_form = MemberRegisterForm(request.POST)
        mp_form = MemberProfileForm(request.POST)
        if mr_form.is_valid() and mp_form.is_valid():
            user = mr_form.save()
            user.profile.age = mp_form.cleaned_data['age']
            user.profile.gender = mp_form.cleaned_data['gender']
            user.profile.address = mp_form.cleaned_data['address']
            user.profile.phone_no = mp_form.cleaned_data['phone_no']
            user.profile.state_of_origin = mp_form.cleaned_data['state_of_origin']
            user.profile.office = mp_form.cleaned_data['office']
            user.profile.qualification = mp_form.cleaned_data['qualification']
            user.profile.status = mp_form.cleaned_data['status']
            user.profile.state_code = mp_form.cleaned_data['state_code']
            user.profile.ppa = mp_form.cleaned_data['ppa']
            user.profile.save()

            username = mr_form.cleaned_data.get('username')
            messages.success(request, f'hello! {username}! your account has been created. \nyou can now login and make posts!')
            return redirect('users:login')
    else:
        mr_form = MemberRegisterForm() 
        mp_form = MemberProfileForm() 
    return render(request, 'users/register.html', {'mr_form':mr_form, 'mp_form':mp_form})


@login_required
def view_profile(request):
    context = {
        'user':request.user
    }
    return render(request, 'users/view_profile.html', context)

def users_profile(request, pk=None):
    user = User.objects.get(pk=pk)
    context = {
        'user':user
    }
    return render(request, 'users/users_profile.html', context)



@login_required
def edit_profile(request):
    if request.method=='POST':
        uu_form = UserUpdateForm(request.POST, instance = request.user)
        pu_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)
        
        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save()
            messages.success(request, f'your profile has been updated!')
            return redirect('users:view_profile')
    else:
        uu_form = UserUpdateForm(instance = request.user)
        pu_form = ProfileUpdateForm(instance = request.user.profile)
        args = {
        'uu_form': uu_form, 
        'pu_form': pu_form
        }
        return render(request,'users/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method=='POST':
        u_form = PasswordChangeForm(data=request.POST, user = request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'your password has been changed!')
            return redirect('users:login')
        else:
            messages.warning(request, f'your password does not match!')
            return redirect('users:change_password')


    else:
        u_form = PasswordChangeForm(user = request.user)
        context = {
        'u_form': u_form
        }
        return render(request,'users/change_password.html',context)



def list_of_members(request):
    users = User.objects.all()
    context = {
        'users': users,
        }
    return render(request,'users/list_of_members.html', context)


def list_of_members_exco(request):
    users = User.objects.all()
    context = {
        'users': users,
        }
    return render(request,'users/list_of_members_exco.html', context)


def list_of_members_nonexco(request):
    users = User.objects.all()
    context = {
        'users': users,
        }
    return render(request,'users/list_of_members_nonexco.html', context)


def list_of_members_passedout(request):
    users = User.objects.all()
    context = {
        'users': users,
        }
    return render(request,'users/list_of_members_passedout.html', context)