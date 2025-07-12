from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Userprofile

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            return redirect('/login/')  # Make sure this URL is correct
    else:
        form = UserCreationForm()  # ← This line should only be in the `else` block

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
