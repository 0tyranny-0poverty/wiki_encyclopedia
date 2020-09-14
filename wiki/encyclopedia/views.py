from . import util
from .models import Entry
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import models as model_forms
from django.template import loader
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy
from random import randint


# Create your views here.

class EntryDetailView(generic.DetailView):
    model = Entry
    slug_field = 'subject'
    slug_url_kwarg = 'subject'

class EntryListView(generic.ListView):
    model = Entry

class EntryCreateView(CreateView):
    model = Entry
    fields = '__all__'

    def form_valid(self, form): # method override
        """If the form is valid, save the associated model."""
        self.object = form.save()
        entry = Entry.objects.get(subject=self.object)
        util.save_entry(entry.subject,entry.content)
        return super().form_valid(form)
    

class EntryUpdateView(UpdateView):
    model = Entry
    fields = '__all__'

    def form_valid(self, form):  # method override
        """If the form is valid, save the associated model."""
        self.object = form.save()
        entry = Entry.objects.get(subject=self.object)
        util.save_entry(entry.subject,entry.content)
        return super().form_valid(form)
    

class EntryDeleteView(DeleteView):
    model = Entry

def get_obj_orlist(request, subject):
    model = Entry
    try:
        entry = Entry.objects.get(subject=subject)
    except Entry.DoesNotExist:
        entries = Entry.objects.filter(subject__icontains=subject)
        return render(request, 'encyclopedia/searchencyc.html', {'entries':entries,'searchtoken':subject} )
    return redirect(entry)


def searchwiki(request):
    searchtoken = request.GET.get('q')
    try:
        entry = Entry.objects.get(subject=searchtoken)
    except Entry.DoesNotExist:
        entries = Entry.objects.filter(subject__icontains=searchtoken)
        contents = Entry.objects.filter(content__icontains=searchtoken)
        return render(request, 'encyclopedia/searchencyc.html', {'entries':entries,'searchtoken':searchtoken, 'contents':contents} )
    return redirect(entry)

def randompage(request):
    """ Returns a random detail page """
    max = Entry.objects.count()
    randid = randint(1,max)
    entry = Entry.objects.get(id=randid)
    return redirect(entry)

def urlguidance(request):
    return render(request,'encyclopedia/urlguidance.html')

