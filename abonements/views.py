from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteVie)
from django import forms
from .models import SubscriptionType


class AbonementForm(forms.ModelForm):
    class Meta:
        model = SubscriptionType
        fields = ['name', 'description', 'period', 'price', 'is_active']


class AbonementListView(ListView):
    model = SubscriptionType
    template_name = 'abonements/abonement_list.html'
    context_object_name = 'abonements'

    def get_queryset(self):
        return SubscriptionType.objects.filter(is_active=True)


class AbonementDetailView(DetailView):
    model = SubscriptionType
    template_name = 'abonements/abonement_detail.html'
    context_object_name = 'abonement'


class AbonementCreateView(CreateView):
    model = SubscriptionType
    form_class = AbonementForm
    template_name = 'abonements/abonement_form.html'
    success_url = reverse_lazy('abonement_list')


class AbonementUpdateView(UpdateView):
    model = SubscriptionType
    form_class = AbonementForm
    template_name = 'abonements/abonement_form.html'
    success_url = reverse_lazy('abonement_list')


class AbonementDeleteView(DeleteView):
    model = SubscriptionType
    template_name = 'abonements/abonement_confirm_delete.html'
    success_url = reverse_lazy('abonement_list')