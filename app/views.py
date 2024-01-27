from django.shortcuts import render,redirect,HttpResponse
from .forms import Dataform
from .models import student_details
# Create your views here.

def data(request):
    if request.method == "POST":
        form = Dataform(request.POST)
        if form.is_valid(): 
            try:
                form.save()
                model = form.instance
                return redirect('show')
            
            except:
                pass

    else:
        form = Dataform()
     
    context = {'form':form}
    return render(request,"index.html",context)


def show(request):
    alldata = student_details.objects.all()
    context={'alldata':alldata}
    return render(request,"show_table.html",context)


def edit(request,id):
    try:
       editdata = student_details.objects.get(id=id)
    except:
         return HttpResponse("Student not found")

    if request.method == "POST":
        form = Dataform(request.POST,instance = editdata)
        if form.is_valid():
            form.save()
            return redirect('show')
    
    else:
        form=Dataform(instance=editdata)
        context = {'form':form }
    return render(request,"edit.html",context)       





def delete(request,id):
    remove = student_details.objects.get(id=id) 
    
    remove.delete() 
    return redirect("show")