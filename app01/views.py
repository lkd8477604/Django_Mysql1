from django.shortcuts import render,HttpResponse
from app01 import forms,models

# Create your views here.
def login_form(request):
    # form = forms.app_forms()
    # if request.method == 'POST':
    print (request.POST)
    form = forms.app_forms(request.POST)
    if form.is_valid():
        print ('form is ok')
        print (form.cleaned_data)
        form_data = form.cleaned_data
        form_data['name'] = request.POST.get('name')
        # login_obj = models.book(**form_data)
        # login_obj.save()
    else:
        print (form.errors)

    login_list = models.book.objects.all()
    return render(request,'app01/login_form.html', {'login_form':form})

def book_model_form(request):
    # form = forms.app_model_form()
    # if request.method == 'POST':
    print (request.POST)
    form = forms.app_model_form(request.POST)
    if form.is_valid():
        print ('form is ok')
        form.save()
    return render(request, 'app01/book_model_form.html', {'book_form':form})