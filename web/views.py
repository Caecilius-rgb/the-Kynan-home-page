from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'web/about.html')

def kynan(request):
    return render(request, 'web/kynan.html')

def secret(request):
    return render(request, 'web/contrail.html')

def nope(request):
    return render(request, 'web/no.html')

def my_404(request):
    return render(request, 'web/404.html')

def secret2(request):
    return render (request, 'web/secret.html')
