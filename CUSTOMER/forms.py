from django import forms
from CUSTOMER.models import SalesPersonModel

TYP_CUS = (
    ('RESTUARANT','Restuarant'),
    ('HOTEL','Hotel'),
    ('CATERING','Catering'),
    ('HOSPITAL,Hospital'),
    ('SCHOOL','School'),
    ('MINIMART','Minimart'),
    ('INDUSTRY','Industry'),
    ('RAN-NEE-KAI-DEE','Ran-Nee-Kai-Dee'),
    ('FRESH SHOP','Fresh Shop'),
    ('OTHER','Other')
)

class SalesPersonChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return obj.SAL_NAM_MDL

class CreateCustomerForm(forms.Form):
    CUS_CV_FORM = forms.CharField(required = True,max_length = 10,label = 'Customer ID')
    CUS_NAM_FORM = forms.CharField(required = True,max_length = 50,label = 'Customer Name')
    CUS_TYP_FORM = forms.MultipleChoiceField(required = True,choices = TYP_CUS,label = 'Customer Type')
    BUS_NAM_FORM = forms.CharField(required = True,max_length = 50),
    SAL_NAM_FORM = SalesPersonChoiceField(
        required = True,
        queryset = SalesPersonModel.objects,
        label = 'Salesperson'
    )