from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import NewPlotReg,APPARTmentCReg,Sales,Employee,User


def showloginhtml(request):
    return render(request,"login.html")


def welcomeuser(request):
    uname=request.POST.get("username")
    pword=request.POST.get("password")
    if uname=="admin" and pword=="admin":
        return render(request,"welcomepage.html")
    else:
       return render(request,"login.html",{"message":"please enter valid userid or password"})


class ViewNewPlotReg(CreateView):
     model = NewPlotReg
     fields="__all__"
     template_name = "newplotreg.html"
     success_url = "/plotdded/"


class UpdatePlot(UpdateView):
     model = NewPlotReg
     fields = ["cost_per_sq_yard","other_expenses","status","total_cost"]
     template_name = "updateplot.html"
     success_url = "/plotadded/"


