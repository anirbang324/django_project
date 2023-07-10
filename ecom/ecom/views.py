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
    contact_form = ContactForm()
    context = {
        'title': 'contact Page',
        'message': 'Contact us',
        'contact_form' : contact_form
    }

    return render(request, "contact/page.html", context)
