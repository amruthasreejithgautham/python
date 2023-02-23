from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Department, Course, Register
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def home (request):
    return render(request,'base.html')
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('username', )
        password = request.POST.get('password', )
        conpass = request.POST.get('conpassword',)
        if password == conpass:
            pd = Register(username=username, password=password)
            pd.save()
            return redirect('/')
        else:
            messages.error(request,'Password not match.')
    return render(request, 'register.html')
def registerform(request):
    qs=Department.objects.all()
    qs1 = Course.objects.all()
    return render(request,'registerform.html',{'qs':qs,'qs1':qs1})
def firstregister(request):
    return render(request,'firstregister.html')
def get_json(request):
    qsval = list(Department.objects.values())
    return JsonResponse({'data':qsval})
