from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
 #   return HttpResponse("Hello Django!!")
# Create your views here.

#クエリパラメータの利用
#def index(request):
    #msg = request.GET['msg']
    #return HttpResponse('you typed: "'+msg+'".')
def home(request):
    return render(request, 'accounts/home.html')


