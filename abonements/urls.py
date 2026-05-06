from django.contrib import admin
from django.urls import path, include

from abonements import views
from views import *

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('abonements/', views.AbonementListView.as_view(), name='abonement_list'),
    path('abonements/create/', views.AbonementCreateView.as_view(), name='abonement_create'),
    path('abonements/<int:pk>/update/', views.AbonementUpdateView.as_view(), name='abonement_update'),
    path('abonements/<int:pk>/delete/', views.AbonementDeleteView.as_view(), name='abonement_delete'),
    path('abonements/<slug:slug>/', views.AbonementDetailView.as_view(), name='abonement_detail'),
]