from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'poll_app/index.html')

# def login(request):
#     return render(request, 'poll_app/login.html')

def login(request):
    if request.method == "POST":
        # Get username and password from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')  # Redirect to a home or dashboard page
        else:
            # Invalid credentials
            messages.error(request, "Invalid username or password.")
    
    # Render login template
    return render(request, 'poll_app/login.html')