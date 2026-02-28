from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
# Create your views here.
def index(request):
    return render(request, 'index.html')

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _("Successfully Sent!"))
        return super().form_valid(form)

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Sent!")
            return redirect(reverse_lazy('home'))
    context  = {

        'form': form
    }
    return render(request, 'contact.html', context)

def error(request):
    return render(request,'404.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')