from django.shortcuts import render
from datetime import datetime,timedelta
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.

def home(request):
    response= render(request,'home.html')
    response.set_cookie('name','Dibbo')
    # response.set_cookie('name','Dibbo Ghosh',max_age=10)
    # response.set_cookie('name','Dibbo Ghosh',expires=datetime.utcnow()+timedelta(days = 7))
    response.set_cookie('name','Dibbo Ghosh',expires=timezone.now()+timedelta(days = 7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    # data = {
    #     'name' : 'Dibbo',
    #     'age' : '23',
    #     'language' : 'English'
    # }
    # request.session.update(data)
    request.session['name'] = 'Dibbo'
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:    
        name = request.session.get('name','Guest')
        # age = request.session.get('age','Guest')
        return render(request,'get_session.html',{'name':name})
    else:
        return HttpResponse('You session has been expired go to login again')

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del.html')