from django.shortcuts import render,redirect,get_object_or_404
from empapp.forms import UsersForm
from empapp.models import Users

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from .forms import UsersForm


def home(request):
    return render(request, "home.html")


def create_emp(request):
    if request.method == "POST":
        form = UsersForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("getall")

    else:
        form = UsersForm()

    return render(request, "emp_form.html", {"form": form})


def getall(request):
    users = Users.objects.all()
    return render(request, "views_emp.html", {"users": users})


def delete(request, id):
    users = get_object_or_404(Users, id=id)

    if request.method == "POST":
        users.delete()
        return redirect("getall")

    return render(request, "delete.html", {"users": users})


def update(request, id):
    users = get_object_or_404(Users, id=id)

    if request.method == "POST":
        form = UsersForm(request.POST, instance=users)

        if form.is_valid():
            form.save()
            return redirect("getall")

    else:
        form = UsersForm(instance=users)

    return render(request, "emp_form.html", {"form": form})