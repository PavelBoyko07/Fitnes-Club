from django.urls import path
from .views import *

urlpatterns = [
    path('', AbonementListView.as_view(), name='abonement_list'),
    path('create/', AbonementCreateView.as_view(), name='abonement_create'),
    path('<int:pk>/', AbonementDetailView.as_view(), name='abonement_detail'),
    path('<int:pk>/update/', AbonementUpdateView.as_view(), name='abonement_update'),
    path('<int:pk>/delete/', AbonementDeleteView.as_view(), name='abonement_delete'),
]