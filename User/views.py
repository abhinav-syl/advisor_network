from django.shortcuts import render

from django.http import HttpResponse
from admin_advisor.models import advisor_name
from .forms import register_form,login_form,book_form
from .models import register,login,booking
# Create your views here.

def register_index(request):

    rg = register.objects.all()

    context = {

        'rg': rg

    }
    return render(request, 'register_index.html', context)

def advisor_index(request):

    ad = advisor_name.objects.all()

    context = {

        'ad': ad

    }
    return render(request, 'advisor_index.html', context)


def register_new(request):
    n=0
    if register.objects.all().exists():
        rg = register.objects.all()
        n = rg.count()
    form = register_form()
    if request.method == 'POST':

        form = register_form(request.POST)

        if form.is_valid():

            register1 = register(

                name=form.cleaned_data["name"],

                email=form.cleaned_data["email"],
                
                password=form.cleaned_data["password"],
                
                user_id = n+1
                

            )
            if register.objects.filter(email=register1.email).exists():
                return HttpResponse("user already exists")
       
            register1.save()


    return render(request, 'register_user.html')

def login_new(request):
    form = login_form()
    user=""
    email = ""
    password=""
    login1 = login(email,password)
    lg = register(user,email,password,0)
    if request.method == 'POST':

        form = login_form(request.POST)

        if form.is_valid():

            login1 = login(

                email=form.cleaned_data["email"],
                
                password=form.cleaned_data["password"],

            )
            login1.save()
    else:
        form = login_form()
    print(email)

    try:
        lg = register.objects.get(email = email)
        if(lg.password!=password):
            return HttpResponse("Authentiation Error",status = 401)
    except register.DoesNotExist:
        lg = lg = register(user,"b",password,0)
        
    context = {

        'lg': lg

    }

    return render(request, 'login_user.html',context)

def book_advisor(request,user_id,advisor_id):
    lg = booking.objects.all()
    n = lg.count()
    form = book_form()
    if request.method == 'POST':

        form = book_form(request.POST)

        if form.is_valid():

            book1 = booking(

                booking_time=form.cleaned_data["booking_time"],
                
                user_id = user_id,
                
                advisor_id = advisor_id,
                
                booking_id = n+1,

            )
            book1.save()
    
    lg = booking.objects.get(booking_id = book1.booking_id)
    context = {

        'lg': lg

    }

    return render(request, 'booking_user.html',context)


#def booking_index(request,user_id):
#    lg = booking.objects.get(user_id = user_id)
#    context = {
#        'lg':lg
#    }
#    return render(request,'booking_index.html',context)