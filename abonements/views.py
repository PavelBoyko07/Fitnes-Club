from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView, UpdateView,DeleteView,TemplateView,)
from .models import SubscriptionType, Trainer, Review
from .forms import AbonementForm, ReviewForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abonements'] = SubscriptionType.objects.filter(is_active=True)[:3]
        context['trainers'] = Trainer.objects.all()
        context['reviews'] = Review.objects.all().order_by('-created_at')[:5]
        return context


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


class TrainerListView(ListView):
    model = Trainer
    template_name = 'trainers/trainer_list.html'
    context_object_name = 'trainers'


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('home')