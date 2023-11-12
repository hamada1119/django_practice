from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from django.forms.widgets import CheckboxInput
from .models import Friend
from .models import Friend,Message


class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ['title','content','friend']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content':forms.Textarea(attrs={'class':'form-control form-control-sm','row':2}),
            'friend':forms.Select(attrs={'class':'form-control form-control-sm'}),
        }



class CheckForm(forms.Form):
    empty=forms.CharField(label='Empty',empty_value=True,\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    min=forms.CharField(label='Min',min_length=10,\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    max=forms.CharField(label='Max',max_length=10,\
        widget=forms.TextInput(attrs={'class':'form-control'}))    
    """"
    p.253
    str=forms.CharField(label='Name',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    """

class FindForm(forms.Form):
    find=forms.CharField(label='Find',required=False,\
        widget=forms.TextInput(attrs={'class':'form-control'}))


class FriendForm(forms.ModelForm):
    class Meta:
        model=Friend
        fields=['name','mail','gender','age','birthday']


class HelloForm(forms.Form):
    name=forms.CharField(label='Name',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail=forms.EmailField(label='Email',\
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender=forms.BooleanField(label='Gender',required=False,\
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label='age',\
        widget=forms.NumberInput(attrs={'class':'form-control'}))        
    birthday=forms.DateField(label='Birth',\
        widget=forms.DateInput(attrs={'class':'form-control'}))



"""""
class HelloForm(forms.Form):
    data=[
        ('one','item 1'),
        ('two','item 2'),
        ('three','item 3'),
        ('four','item 4'),
        ('five','item 5'),
    ]
    choice = forms.MultipleChoiceField(label='radio',\
        choices=data,widget=forms.SelectMultiple(attrs={'size' : 6}))
"""

"""
class HelloForm(forms.Form):
    name = forms.CharField(label='name',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='mail',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age',\
        widget=forms.NumberInput(attrs={'class':'form-control'}))
"""
