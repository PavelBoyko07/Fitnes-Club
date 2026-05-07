from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView,DeleteView,UpdateView,ListView,DetailView,)
from django.urls import reverse_lazy
from django import forms
from gprof2dot import Object
from .models import Subscription

from abonements.models import Category, SubscriptionType

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'slug', 'is_active']
#
#
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = SubscriptionType
#         fields = ['name','slug','category','price','duration_days','is_active',]
#
# def category_list(request):
#     context = {
#         'abonements': Category.objects.all(),
#     }
#     return render(request, 'fitness/abonements_list.html', context)
#
#
# class CategoryCreateView(CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'fitness/abonements_form.html'
#     success_url = reverse_lazy('category_list')
#
#
# class CategoryDeleteView(DeleteView):
#     model = Category
#     template_name = 'fitness/abonements_confirm_delete.html'
#     success_url = reverse_lazy('category_list')
#
#
# class CategoryUpdateView(UpdateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'fitness/abonements_form.html'
#     success_url = reverse_lazy('category_list')
#
#
# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     products = category.subscriptiontype_set.filter(is_active=True)
#     context = {
#         'category': category,
#         'products': products,
#     }
#     return render(request, 'fitness/detail.html', context)
#
# class AbonementListView(ListView):
#     model = SubscriptionType
#     template_name = 'fitness/abonements_list.html'
#     context_object_name = 'products'
#     paginate_by = 12
#
#     def get_queryset(self):
#         queryset = SubscriptionType.objects.filter(is_active=True)
#         category_slug = self.kwargs.get('category_slug')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.filter(is_active=True)
#         context['category'] = None
#         category_slug = self.kwargs.get('category_slug')
#         if category_slug:
#             context['category'] = get_object_or_404(
#                 Category,
#                 slug=category_slug,
#                 is_active=True
#             )
#         return context
#
#
# class AbonementCreateView(CreateView):
#     model = SubscriptionType
#     form_class = ProductForm
#     template_name = 'fitness/abonement_form.html'
#     success_url = reverse_lazy('abonement_list')
#
#
# class AbonementUpdateView(UpdateView):
#     model = SubscriptionType
#     form_class = ProductForm
#     template_name = 'fitness/abonement_form.html'
#     success_url = reverse_lazy('abonement_list')
#
#
# class AbonementDeleteView(DeleteView):
#     model = SubscriptionType
#     template_name = 'fitness/abonement_confirm_delete.html'
#     success_url = reverse_lazy('abonement_list')
#
#
# class AbonementDetailView(DetailView):
#     model = SubscriptionType
#     template_name = 'fitness/abonement_detail.html'
#     context_object_name = 'product'
#
#     def get_queryset(self):
#         return SubscriptionType.objects.filter(is_active=True)
#
#     def get_object(self, queryset=None):
#         slug = self.kwargs.get('slug')
#         if queryset is None:
#             queryset = self.get_queryset()
#         if slug:
#             return get_object_or_404(queryset, slug=slug, is_active=True)
#         return super().get_object(queryset)
#
# def abonements_list(request):
#     context = {
#         'products': SubscriptionType.objects.filter(is_active=True),
#         'categories': Category.objects.filter(is_active=True),
#     }
#     return render(request, 'fitness/abonements_list.html', context)
#
#
# class Products:
#     pass
#
#
# def get_queryset(self):
#         return Products.objects.filter(is_active=True)

def home(request):
    abonements = Object.Subscription.objects.all()

    return render(request, 'index.html', {'abonements': abonements})