from django.contrib import admin
from .models import Allgroups, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class AllgroupsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        ]

admin.site.register(Allgroups, AllgroupsAdmin)
admin.site.register(Comment)

