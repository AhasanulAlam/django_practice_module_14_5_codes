from django.shortcuts import render
from . forms import contactForm

# Create your views here.
def home(request):
    return render(request, './home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        rate = request.POST.get('rating')
        return render(request, './about.html', {'name': name, 'email': email, 'rate': rate})
    else:
        return render(request, './about.html')

def submit_form(request):
    return render(request, './form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, './django_form.html', {'form' : form})
    else:
        form = contactForm()    
    return render(request, './django_form.html', {'form' : form})
    

