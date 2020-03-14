from django.contrib import admin
from .models import UserProfile, Receipt
# Register your models here.

class ReceiptView(admin.ModelAdmin):
    list_display = ('user', 'purchase_date', 'amount',)
    list_filter = ('purchase_date', )
    date_hierarchy = 'purchase_date'

class UserProfileView(admin.ModelAdmin):
    list_display = ('user', 'join_date', 'membership_status',)
    date_hierarchy = 'join_date'

admin.site.register(UserProfile, UserProfileView)
admin.site.register(Receipt, ReceiptView)
