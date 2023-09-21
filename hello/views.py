#from typing import Generic
from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse, request
#from django.views.generic import TemplateView
from django.shortcuts import redirect
#from .forms import HelloForm
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from .forms import CheckForm
from django.core.paginator import Paginator
from .models import Friend,Message
from .forms import FriendForm,MessageForm

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend


def message(request,page=1):
    if(request.method=='POST'):
        obj=Message()
        form=MessageForm(request.POST,instance=obj)
        form.save()
    data=Message.objects.all().reverse()
    paginator=Paginator(data,5)
    params={
        'title':'Message',
        'title':'MessageForm',
        'title':'paginator.get_page(page)',
    }
    return render(request,'hello/message.html',params)
    


def check(request):
    params={
        'title':'Hello',
        'message':'check validation',
        'form':FriendForm(),
    }
    if(request.method=='POST'):
        obj=Friend()
        form=FriendForm(request.POST,instance=obj)
        params['form']=form
        if(form.is_valid()):
            params['message']='OK!'            
        else :
            params['message']='no good.'
    return render(request,'hello/check.html',params)            


def find(request):
    if(request.method=='POST'):
        form=FindForm(request.POST)
        find=request.POST['find']
        list=find.split()
        data=Friend.objects.filter(name__in=list)
        msg='Result:'+str(data.count())
    else :
        msg='search words...'
        form=FindForm()
        data=Friend.objects.all()
    params ={
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'hello/find.html',params)



def index(request,num=1):
    #data=Friend.objects.all().order_by('age')#並び変え
    data = Friend.objects.all()
    page = Paginator(data,3)
    params={
        'title':'Hello',
        'message':'',
        'data':page.get_page(num),
    }
    return render(request,'hello/index.html',params)

#create model
def create(request):
    if(request.method=='POST'):
        obj=Friend()
        friend=FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/hello')
    params={
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request,'hello/create.html',params)

def edit(request,num):
    obj=Friend.objects.get(id=num)
    if(request.method=='POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save
        return redirect(to='/hello')
    params={
        'title':'Hello',
        'id':num,
        'form':FriendForm(instance=obj),
    }    
    return render(request,'hello/edit.html',params)

def delete(request,num):
    friend = Friend.objects.get(id=num)
    if(request.method=='POST'):
        friend.delete()
        return redirect(to='/hello')
    params={
        'title':'Hello',
        'id':num,
        'obj':friend,
    }
    return render(request,'hello/delete.html',params)    



""""
def create(request):
    params ={
        'title':'Hello',
        'form':HelloForm(),
    }
    if(request.method == 'POST'):
        name=request.POST['name']
        mail=request.POST['mail']
        gender='gender' in request.POST
        age = int(request.POST['age'])
        birth=request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,\
            age=age,birthday=birth)
        friend.save()
        return redirect(to='/hello')    
 
    return render(request,'hello/create.html',params)
"""


""""
    if(request.method=='POST'):
        num=request.POST['id']
        item =Friend.objects.get(id=num)
        params['data']=[item]
        params['form']=HelloForm(request.POST)
    else:
        params['data']=Friend.objects.all()

class HelloView(TemplateView):
    def __init__(self):
        self.params={
            'title':'お問い合わせフォーム',
            'form':HelloForm(),
            'result':None
        }
    
    def get(self,request):
        return render(request,'hello/index.html',self.params)
    
 
    def post(self,request):
        ch =request.POST.getlist('choice')
        result='<ol class="list-group"><b>selected:</b>'
        for item in ch:
            result +='<li class="list-group-item">'+item+'</li>'
        result +='</ol>'
        self.params['result']=result
        self.params['form']=HelloForm(request.POST)                  
        return render(request,'hello/index.html',self.params)
"""