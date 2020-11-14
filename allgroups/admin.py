from django.contrib import admin
from .models import Allgroups, Comment, userlist

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
class userlistInline(admin.StackedInline):
    model = userlist
    extra = 0

    
class AllgroupsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline, userlistInline
        ]

admin.site.register(Allgroups, AllgroupsAdmin)
admin.site.register(Comment)
admin.site.register(userlist)

