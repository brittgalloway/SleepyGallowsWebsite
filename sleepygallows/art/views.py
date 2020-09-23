from django.shortcuts import render

def index(request):
    return render(request, 'art/index.html')
def brittney(request):
    return render(request, 'art/brittney.html')
def sketchbook(request):
    return render(request, 'art/sketchbook.html')
def papercuts(request):
    return render(request, 'art/papercuts.html')
def crystal(request):
    return render(request, 'art/crystal.html')
def illustration(request):
    return render(request, 'art/illustration.html')
def visdev(request):
    return render(request, 'art/visdev.html')
