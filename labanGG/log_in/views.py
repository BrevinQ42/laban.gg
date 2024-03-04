from django.shortcuts import render

# Create your views here.

def log_in_view(request):
    
    return render(request, 'log_in/log_in.html', {'form': form})