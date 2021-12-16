from django.contrib import admin
from base.models import Message


@admin.register(Message)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','created_at']

