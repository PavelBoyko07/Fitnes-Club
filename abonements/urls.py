from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('abonements/', AbonementListView.as_view(), name='abonement_list'),
    path('abonements/create/', AbonementCreateView.as_view(), name='abonement_create'),
    path('abonements/<int:pk>/', AbonementDetailView.as_view(), name='abonement_detail'),
    path('abonements/<int:pk>/update/', AbonementUpdateView.as_view(), name='abonement_update'),
    path('abonements/<int:pk>/delete/', AbonementDeleteView.as_view(), name='abonement_delete'),
    path('trainers/', TrainerListView.as_view(), name='trainer_list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
]