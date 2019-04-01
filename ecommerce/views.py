from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        'title': 'Hello World',
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {

    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'content': 'Welcome to contact Page',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('name'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    # print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data.get('username'))
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            # context["form"] = LoginForm()
            return redirect("/")
        else:
            print('error')
            # No backend authenticated the credentials

    return render(request, "auth/login.html", context)


def logout_page(request):
    return render(request, "auth/logout.html", {})
