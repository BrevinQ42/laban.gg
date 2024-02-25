from django.shortcuts import render
from django.http import HttpResponse

from .forms import AccountForm
from .models import Account

# Create your views here.
# def index(request):
#     return HttpResponse('Hello World! This came from the index view')


def register_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_account = form.save()
    else:
        form = AccountForm()
    return render(request, 'register/register.html', {'form': form})
