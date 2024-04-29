from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Welcome to My Website',
        'content': 'This is a dynamic content generated by Django!',
    }
    return render(request, 'home.html', context)



from app1.models import Places
def place(request):
    p=Places.objects.all()
    return render(request,'places.html',{'p':p})