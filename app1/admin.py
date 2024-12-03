from django.contrib import admin
from . import models
from .models import StudyContent

admin.site.register(StudyContent)

class stickyNotesAdmin (admin.ModelAdmin):
    list_display= ('title',)

admin.site.register(models.stickyNote,stickyNotesAdmin)

admin.site.register(models.Notebook)

