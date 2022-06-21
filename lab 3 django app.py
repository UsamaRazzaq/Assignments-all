from django.shortcuts import render , HttpResponse

# creatre view here:

def index(request):
    if request.ethod =='POST':
        d={'n': "You are reqister with our website", 'b':['asad','asad.arshad']}
        return render(request, 'main.html', d)
    else:
        d={'n':'asad', 'b':['C++','java','python']}
        return render(request,'login.html',d)
