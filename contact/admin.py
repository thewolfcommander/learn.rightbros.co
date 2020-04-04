from django.contrib import admin

from contact.models import EnrollForDemo

@admin.register(EnrollForDemo)
class EnrollForDemoAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'father_name', 'mobile_number', 'student']
    list_filter = ['student', 'timestamp', 'updated', 'is_approved']
    search_fields = ['first_name', 'last_name', 'email', 'father_name']