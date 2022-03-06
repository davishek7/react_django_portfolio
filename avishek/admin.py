from django.contrib import admin
from .models import Project, Contact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'details', 'image', 'live_url', 'github_repo']
    search_fields = ['title', 'details', 'image', 'live_url', 'github_repo']

    class Meta:
        model = Project


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'details']
    search_fields = ['name', 'subject', 'email', 'details']

    class Meta:
        model = Contact