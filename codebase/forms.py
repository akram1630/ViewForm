from django import forms
from django.forms.widgets import Widget
from .models import CRUD

#form is to create our forms instead of defaul which is created by model
              
#make this class model_form
class CRUDFORM(forms.ModelForm):
     #widget <=> tag  , attrs <=> attribu
  name = forms.CharField(widget = forms.TextInput(attrs=
                                                {'class':'form-control',
                                                 'placeholder':'name'}
                                                 ) , 
  )
  age = forms.CharField(widget = forms.TextInput(attrs=
                                                 {'class':'form-control',
                                                  'placeholder':'age'}
                                                  ) 
  )                      
  level = forms.CharField(widget = forms.Textarea(attrs=
                                                 {'class':'form-control',
                                                  'placeholder':'level'}) 
  )
  class Meta: # the class who receives the data of forms
    model = CRUD
    fields = ['name','age','level']