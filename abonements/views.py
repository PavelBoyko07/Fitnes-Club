from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from django.contrib import messages
from .models import SubscriptionType, Trainer, Review, Category, ContactMessage
from .forms import ReviewForm, ContactForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abonements'] = SubscriptionType.objects.filter(is_active=True)[:3]
        context['trainers'] = Trainer.objects.filter(is_active=True)[:4]
        context['reviews'] = Review.objects.filter(is_moderated=True)[:6]
        context['popular_abonement'] = SubscriptionType.objects.filter(is_active=True, is_popular=True).first()
        return context


class AbonementListView(ListView):
    model = SubscriptionType
    template_name = 'abonements/abonement_list.html'
    context_object_name = 'abonements'

    def get_queryset(self):
        return SubscriptionType.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AbonementDetailView(DetailView):
    model = SubscriptionType
    template_name = 'abonements/abonement_detail.html'
    context_object_name = 'abonement'


class TrainerListView(ListView):
    model = Trainer
    template_name = 'trainers/trainer_list.html'
    context_object_name = 'trainers'

    def get_queryset(self):
        return Trainer.objects.filter(is_active=True)


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Спасибо за отзыв! Он будет опубликован после проверки.')
        return super().form_valid(form)


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        ContactMessage.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            message=form.cleaned_data['message']
        )
        messages.success(self.request, 'Сообщение отправлено! Мы свяжемся с вами.')
        return super().form_valid(form)