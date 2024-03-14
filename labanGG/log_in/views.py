from django.shortcuts import redirect, render

from .forms import LogInForm
# Create your views here.

def log_in_view(request):
    if request.method == 'POST':
        if 'form_submit' in request.POST:
            form = LogInForm(request.POST)
            if form.is_valid():
                return redirect('/games')
    else:
        form = LogInForm()
    return render(request, 'log_in/log_in.html', {'form': form})