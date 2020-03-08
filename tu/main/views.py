from django.shortcuts import render, redirect
import django.forms as forms
from . import models

# Create your views here.


def new(request):
    class Form(forms.ModelForm):
        class Meta:
            model = models.Appl
            fields = '__all__'

    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()

    return render(request, template_name='new.html', context={'form': form,
                                                              'action': 'post'})


def home(request):
    """
    Список заявок в табличной форме
    :param request:
    :return:
    """
    return render(request, template_name='home.html', context={})
