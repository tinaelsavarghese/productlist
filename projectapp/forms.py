from django import forms
from .models import products
class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ('edescription','ebaseunitofmeasure','eprojectunitofmeasure','econversionfactor','econtractingentryref','ematerialtype','emasterformatcode','euniformat','eRBScode','eWBSCODE')
        labels = {'edescription':'description',
                  'ebaseunitofmeasure':'baseunitofmeasure',
                  'eprojectunitofmeasure': 'projectunitofmeasure',
                  'econversionfactor': 'conversionfactor',
                  'econtractingentryref':'contractingentryref',
                  'ematerialtype':'materialtype',
                  'emasterformatcode':'masterformatcode',
                  'euniformat':'uniformat',
                  'eRBScode':'RBScode',
                  'eWBSCODE':'WBSCODE'
                  }
