from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .forms import SignupForm, EditProfileForm, EditUserForm
from .models import Profile
from django.contrib import messages
from services.models import croppredictions,waterpredictions


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Registration sucessful")
            login(request, user)
            return redirect('home:home_render')
        else:
            messages.error(request, form.errors)
            return redirect('accounts:signup')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})



'''
predictList = croppredictions.objects.filter(user=current_user)
    paginator = Paginator(PredictList, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number
'''



def profile(request):
    profile = Profile.objects.get(user=request.user)
    current_user = request.user

    cropPredictList = croppredictions.objects.filter(user=current_user).order_by('-date')
    croppaginator = Paginator(cropPredictList, 4)
    page_number_crop = request.GET.get('page')
    page_obj_crop = croppaginator.get_page(page_number_crop) 
    
    waterPredictList = waterpredictions.objects.filter(user=current_user).order_by('-date')
    waterpaginator = Paginator(waterPredictList, 4)
    page_number_water = request.GET.get('page')
    page_obj_water = waterpaginator.get_page(page_number_water) 
    return render(request, 'accounts/profile.html', {'profile': profile, 'suggest': page_obj_crop,'predict':page_obj_water})
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = EditUserForm(
            request.POST, request.FILES, instance=request.user)
        profileform = EditProfileForm(
            request.POST, request.FILES, instance=profile)
        if userform.is_valid and profileform:
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            userform.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = EditUserForm(instance=request.user)
        profileform = EditProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})


def logout_view(request):
    logout(request)
