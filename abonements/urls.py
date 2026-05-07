from django.urls import path
from . import views

app_name = 'abonements'

urlpatterns = [
    path('', views.home, name='home'),
    # path('categories/', views.category_list, name='category_list'),
    # path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    # path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    # path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    # path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    # path('abonements/', views.AbonementListView.as_view(), name='abonement_list'),
    # path('abonements/create/', views.AbonementCreateView.as_view(), name='abonement_create'),
    # path('abonements/<int:pk>/', views.AbonementDetailView.as_view(), name='abonement_detail'),
    # path('abonements/<int:pk>/update/', views.AbonementUpdateView.as_view(), name='abonement_update'),
    # path('abonements/<int:pk>/delete/', views.AbonementDeleteView.as_view(), name='abonement_delete'),
    # path('cart/', views.cart_view, name='cart_view'),
    # path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    # path('users/', views.users_list, name='users_list'),
    # path('reviews/', views.reviews_list, name='reviews_list'),
    # path('reviews/add/', views.add_review, name='add_review'),
]