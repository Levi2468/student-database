from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from.models import Details
from.forms import Formfield


def registry(request):
    if request.method=="POST":
        form = Formfield(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Formfield()
        return render(request,'register.html',{'form':form})

def hom(request):
    stored=Details.objects.all()
    return render(request, 'interface.html', {'stored':stored})


def edits(request, pk):
    item = get_object_or_404(Details, pk=pk)
    if request.method == "POST":
        form = Formfield(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Formfield(instance=item)
        return render(request, 'edit.html', {'form': form})


def delete(request,pk):
    item=get_object_or_404(Details,pk=pk)
    item.delete()
    return redirect('home')
