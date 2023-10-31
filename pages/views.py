from django.shortcuts import render, redirect
from .forms import bookTablesForm
from django.contrib import messages


# Create your views here.
def index(request):
    form = bookTablesForm()
    if request.method == 'POST':
        form = bookTablesForm(request.POST)
        if form.is_valid():
            form.save()
            form = bookTablesForm()
            messages.success(request, 'Your table has been booked successfully')
            return redirect('index')

    context = {'form': form}

    return render(request,'pages/index.html', context)


def login_page(request):
    return render(request,'pages/login_page.html')