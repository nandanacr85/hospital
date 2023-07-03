from django.shortcuts import render
from django.http import HttpResponse
from . models import Department, Doctor
from . forms import BookingForm

def index(request):
    return render(request,"index.html")
def department(request):
    department=Department.objects.all()
    return render(request,"department.html",{'department':department})
def doctor(request):
    doctor=Doctor.objects.all()
    return render(request,"doctor.html",{'doctor':doctor})
def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> thankyou </h1>')
    return  render(request,'booking.html',{'form':form})
        

    