from django.contrib import admin
from .models import Category, SubscriptionType, Trainer, Review, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'period_days', 'is_active', 'is_popular']
    list_filter = ['is_active', 'is_popular', 'has_gym', 'has_pool']
    search_fields = ['name', 'description']
    list_editable = ['price', 'is_active', 'is_popular']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'price', 'old_price', 'period_days', 'visits_count')
        }),
        ('Визуал и категория', {
            'fields': ('image', 'category')
        }),
        ('Доступные зоны', {
            'fields': ('has_gym', 'has_pool', 'has_group', 'has_spa')
        }),
        ('Дополнительно', {
            'fields': ('features', 'is_active', 'is_popular')
        }),
    )

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty', 'experience_years', 'is_active', 'order']
    list_filter = ['is_active', 'specialty']
    search_fields = ['name', 'specialty']
    list_editable = ['order', 'is_active']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'created_at', 'is_moderated']
    list_filter = ['rating', 'is_moderated', 'created_at']
    search_fields = ['name', 'text']
    list_editable = ['is_moderated']
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_moderated=True)
    approve_reviews.short_description = "Одобрить выбранные отзывы"

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']
