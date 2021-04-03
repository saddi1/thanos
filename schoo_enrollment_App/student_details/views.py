from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Student
from .forms import CreatestudentForm


# Create your views here.

def dashboard(request):
    context = {}
    context["dataset"] = Student.objects.all()
    return render(request, "dashboard.html", context)


def create_student(request):
    context = {}
    form = CreatestudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context['form'] = form
    return render(request, "newStudent.html", context)


def detail_view(request, pk):
    data = Student.objects.get(pk=pk)
    print(data)
    form = CreatestudentForm(data)
    return render(request, "detail.html", {'data': data})
