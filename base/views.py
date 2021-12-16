from django.views.generic import TemplateView,View
from django.shortcuts import render,redirect
from base.models import Message
from django.contrib import messages


class About(TemplateView):
    template_name = 'home/about.html'


class Index(TemplateView):
    template_name = 'home/index.html'


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/contact.html')

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Message.objects.create(first_name=first_name ,last_name=last_name, email=email, message=message,phone=phone)
        messages.success(request, 'Message Was Submitted successfully, we will respond shortly')
        return redirect('base:contact')