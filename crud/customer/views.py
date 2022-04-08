from django.shortcuts import render, redirect  
from customer.forms import CustomerForm  
from customer.models import Customer  


def createCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()  
                return redirect(readCustomer)  
            except:  
                pass
    else:
        form = CustomerForm()  
    return render(request,"create.html", {'form':form})

def readCustomer(request):
    customers = Customer.objects.all()  
    return render(request,"read.html", {'customers':customers})

def editCustomer(request, id):
    customer = Customer.objects.get(id=id)  
    return render(request,'update.html', {'customer':customer})

def updateCustomer(request, id):
    customer = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():
        form.save()
        return redirect(readCustomer)  
    return render(request, 'update.html', {'customer': customer})

def destroyCustomer(request, id):
    customer = Customer.objects.get(id=id)  
    customer.delete()  
    return redirect(readCustomer)