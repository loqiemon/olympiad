from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'institution_name', 'email', 'phone_number')
    list_filter = ('email', 'institution_name')
    list_max_show_all = 30
    list_per_page = 30
    ordering = ['full_name',]
    search_fields = ['full_name', 'phone_number', 'email']
    search_help_text = "Поиск"


admin.site.register(CustomUser, CustomUserAdmin)




