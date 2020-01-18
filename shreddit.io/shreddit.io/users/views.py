from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! You can now login as {username}!')
            return redirect('login')
    else:
        form = UserSignupForm()

    return render(request, 'users/signup.html', {'form':form})
