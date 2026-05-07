from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('abonements/', views.AbonementListView.as_view(), name='abonement_list'),
    path('abonements/<int:pk>/', views.AbonementDetailView.as_view(), name='abonement_detail'),
    path('trainers/', views.TrainerListView.as_view(), name='trainer_list'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)