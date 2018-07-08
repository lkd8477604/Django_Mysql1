"""#_author:John
   #date:{date}
"""
from django import forms
from app01 import models

class login_for(forms.Form):
    name = forms.CharField(max_length=32)
    lisher = forms.CharField(max_length=10,
                                error_messages={'required':'不能为空',
                                                'max_length':u'标题不能超过10个字符',}
                            )

    # femal = forms.CharField(widget=forms.Select)
class app_forms(forms.Form):
    name = forms.CharField()
    lisher = forms.CharField(max_length=10,
                                error_messages={'required':'不能为空',
                                                'max_length':u'标题不能超过10个字符',})



class app_model_form(forms.ModelForm):

    class Meta:
        model = models.book
        # fields = ('name','authors', 'publisher')
        exclude =()
        wedits = {
            'name': forms.TextInput(attrs={'class':'forms-control'}),
        }
