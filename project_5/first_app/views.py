from django.shortcuts import render,redirect
from . forms import contactForm,studentForm
from . forms import passwordform
# Create your views here.

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'about.html',{'name':name,'email': email,'select':select})
    else:
        return render(request,'about.html')

def submit_form(request):
    return render(request,'forms.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name ,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'Djangoform.html',{'form':form})
    else:
        form = contactForm()
    return render(request,'Djangoform.html',{'form':form})

def Studentform(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'Studentform.html',{'form':form})
            # return render(request, 'Studentform.html', {'form': form})
    else:
        form = studentForm()
    return render(request, 'Studentform.html', {'form': form})

def PasswordForm(request):
    if request.method == 'POST':
        form = passwordform(request.POST) 
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordform() 
    return render(request, 'passwordform.html', {'form': form})

