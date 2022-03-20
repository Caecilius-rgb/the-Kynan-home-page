from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'web/about.html')

def kynan(request):
    return render(request, 'web/kynan.html')

def secret(request):
    return render(request, 'web/contrail.html')
