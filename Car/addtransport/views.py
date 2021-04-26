from django.shortcuts import render,redirect
from .models import Transport
from .forms import TransportAddForm
from django.contrib import messages
# Create your views here.

def add_transport(request):
    form = TransportAddForm()
    if request.method =="POST":
        form = TransportAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            messages.success(request, ' Transport Saved ')
            return redirect('add_transport')
        else:
            messages.success(request, 'Error found ')
            print(form.errors)
            print("not saved")
            return redirect('add_transport')
    return render(request,'add_transport.html',context = {'form':form})




