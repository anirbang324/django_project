from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    context = {
        'title': 'home Page',
        'message': 'first page'
    }
    return render(request, "home.html", context)


def about_page(request):
    context = {
        'title': 'About Page',
        'message': 'learn more about us'
    }
    return render(request, "home.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'contact Page',
        'message': 'Contact us',
        'contact_form' : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/page.html", context)
