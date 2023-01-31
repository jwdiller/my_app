from contextlib import _RedirectStream
from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Item has been Added'))
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items' : all_items})

def about(request):
    my_name = "James Diller"
    return render(request, 'about.html', {'name': my_name})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has Been Deleted'))
	return redirect('home')