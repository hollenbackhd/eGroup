from django.contrib import admin
from .models import Allgroups, Comment, userList

class CommentInline(admin.TabularInline):
    model = Comment
class userListInline(admin.TabularInline):
    model = userList

    
class AllgroupsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline, userListInline
        ]

admin.site.register(Allgroups, AllgroupsAdmin)
admin.site.register(Comment)
admin.site.register(userList)

