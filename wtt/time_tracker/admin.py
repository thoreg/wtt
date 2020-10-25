from django.contrib import admin
from time_tracker.models import Project, Entry


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    model = Project


class EntryAdmin(admin.ModelAdmin):
    list_display = ('project', 'start_at', 'end_at', 'duration_in_minutes')
    model = Entry


admin.site.register(Entry, EntryAdmin)
admin.site.register(Project, ProjectAdmin)

