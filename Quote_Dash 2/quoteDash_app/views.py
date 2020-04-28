from django.shortcuts import render, redirect
from .models import User, Quote, Login
from django.contrib import messages

def index(request):
    return render(request, 'main.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'my_quotes': Quote.objects.all()
    }
    return render(request, 'uDash.html', context)

def register(request):
    print(request.POST)
    errors = User.objects.user_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    new_user = User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email=request.POST['email'], password=request.POST['pass'])
    request.session['user'] = new_user.last_name
    request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    errors = Login.objects.login_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    logged_user = User.objects.filter(email=request.POST['email'])

    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pass']:
            request.session['user'] = logged_user.last_name
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def logout(request):
    print(request.session)
    request.session.flush()
    return redirect('/')

def quote(request):
    print(quote)
    errors = Quote.objects.quote_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/success')
    Quote.objects.create(quote=request.POST['q_desc'], author=User.objects.get(id=request.session['id']))
    return redirect('/success')

def profile(request, id):
    context = {
        'author': User.objects.get(id=id)
    }
    return render(request, 'Qprofile.html', context)

def likeQ(request, id):
    print(likeQ)
    quote_liked = Quote.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    quote_liked.user_likes.add(user_liking)
    return redirect('/success')

def deleteQ(request, id):
    erase = Quote.objects.get(id=id)
    erase.delete()
    return redirect('/success')

def back(request):
    return redirect('/success')

def editPRO(request):
    print(editPRO)
    return render(request, 'eProfile.html')

def edit(request, id):
    errors = Edit.objects.edit_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/editPRO')
    edit_user = User.objects.get(id=id)
    edit_user.first_name = request.POST['f_name']
    edit_user.last_name = request.POST['l_name']
    edit_user.email = request.POST['email']
    edit_user.save()
    return redirect('/editPRO')

def editForm(request):
    return redirect('/editPRO')

