from django.contrib import admin

from . import models

@admin.register(models.PostcodeArea)
class PostcodeAreaAdmin(admin.ModelAdmin):
    pass
