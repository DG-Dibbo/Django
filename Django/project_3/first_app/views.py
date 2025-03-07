from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author' : 'Author', 'age' : 15, 'lst' : ['Python','is','Fun'],
         'birthday':datetime.datetime.now(),'sentence':'Hi I am Dibbo Ghosh.'
         'I am a student in bsc in cse.','courses' : [
        {
            'id': 1,
            'name': 'Python',
            'fee': 15000
        },
        {
            'id': 2,
            'name' : 'Django',
            'fee': 25000
        },
        {
            'id': 3,
            'name' : 'HTML/CSS',
            'fee': 10000
        },

    ]}
    return render(request,'home.html',d)