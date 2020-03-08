from django.shortcuts import render, redirect, reverse
import django.forms as forms
from . import models

# Create your views here.


def new(request):
    """
    Создание новой заявки
    :param request:
    :return:
    """
    class Form(forms.ModelForm):
        class Meta:
            model = models.Appl
            fields = '__all__'

    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    context = {'form': form, 'method':'post'}
    return render(request, template_name='new.html', context=context)


def home(request):
    """
    заявки
    Список заявок в табличной форме
    :param request:
    :return:
    """
    qs = models.Appl.objects.all()
    context = {}
    context.update(qs=qs)
    return render(request, template_name='home.html', context=context)
