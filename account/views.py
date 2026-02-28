from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from account.forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

# Create your views here.
def signin(request):
    form = SignInForm
    if request.method == "POST":
        form = SignInForm(data = request.POST)
        if form.is_valid():
            user = authenticate(request, email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            django_login(request, user)
            if not user:
                pass
            return redirect(reverse_lazy('home'))         

    context = {
        'form': form
    }
    return render(request, 'signin.html', context)

def signup(request):
    form = SignUpForm
    if request.method ==  "POST":
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse_lazy('signin'))
    context = {

        'form':form 
    }
    return render(request, 'signup.html', context)

def wish_list(request): 
    return render(request, 'wish-list.html')