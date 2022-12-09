from django.shortcuts import render
from CUSTOMER.forms import CreateCustomerForm
from CUSTOMER.models import CustomerInputModel

# Create your views here.

def Customer(request):
    return render(request,'Customer/Customer.html')

def CustomerInput(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cus_model = CustomerInputModel()

            cus_model.CUS_CV_MDL = data['CUS_CV_FORM']
            cus_model.CUS_NAM_MDL = data['CUS_NAM_FORM']
            cus_model.CUS_TYP_MDL = data['CUS_TYP_FORM']
            cus_model.BUS_NAM_MDL = data['BUS_NAM_FORM']
            cus_model.SAL_NAM_MDL = data['SAL_NAM_FORM'].SAL_NAM_MDL
            cus_model.save()
    form = CreateCustomerForm()
    context = {'form':form}
    return render(request,'Customer/CreateCustomerPage.html',context)
