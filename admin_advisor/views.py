from django.shortcuts import render

from admin_advisor.models import advisor_name
from .forms import advisor_form
# Create your views here.

def advisor_index(request):
    ai =  advisor_name.objects.all()
    n = ai.count()
    form = advisor_form()
    if request.method == 'POST':

        form = advisor_form(request.POST)

        if form.is_valid():

            advisor_new = advisor_name(

                name=form.cleaned_data["name"],

                url=form.cleaned_data["url"],
                
                advisor_id = n+1,


            )

            advisor_name.save()

    ad = advisor_name.objects.all()

    context = {

        'ad': ad

    }
    return render(request, 'advisor_index.html', context)

    #return render(request, 'advisor_index.html', context)


def add_name(request):
    ai =  advisor_name.objects.all()
    n = ai.count()
    form = advisor_form()
    if request.method == 'POST':

        form = advisor_form(request.POST)

        if form.is_valid():

            advisor_new = advisor_name(

                name=form.cleaned_data["name"],

                url=form.cleaned_data["url"],
                
                advisor_id = n+1,


            )

            advisor_new.save()
    ad = advisor_name.objects.all()

    context = {

             'ad': ad
        }
        
    return render(request, 'add_advisor.html', context)
