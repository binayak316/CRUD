from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import curdForm, CreateUserForm
from .models import curdmodels
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    post = curdmodels.objects.all()
    context ={
        'post': post,
    }

    return render(request, 'curdapp/index.html', context)
@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = curdForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Your Post has been Successfully Posted")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Your Post can't be Posed")

    else:
        form = curdForm()

    content = {
        'form': form,
    }
    return render(request, "curdapp/add.html", content)



@login_required(login_url='login')
def delete(request, id):
    object = curdmodels.objects.get(id=id)
    if request.method == 'POST':
        object.delete()
        messages.success(request, 'Your Post Has Been Successfully Deleted')
        return HttpResponseRedirect('/')

    context = {
        'object': object,
    }

    return render(request, 'curdapp/delete.html', context)



@login_required(login_url='login')
def update(request,id):
    object = curdmodels.objects.get(id=id)
    form = curdForm(instance=object)
    if request.method == 'POST':
        form = curdForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Post Is Successfully Updated')
            return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request, 'curdapp/update.html', context)



def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)


                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'curdapp/register.html', context )

def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Logged-in')
                return HttpResponseRedirect('/')
            else:
                messages.info(request, 'You entered wrong username or password')
        context = {

        }
        return render(request, 'curdapp/login.html', context)


def Logout(request):
    logout(request)
    return redirect('login')


























