from django.contrib import admin
from .models import Allgroups, Comment, userlist, Comment1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
class userlistInline(admin.StackedInline):
    model = userlist
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'allgroups', 'created', 'active')
    list_filter = ('active','created', 'updated')
    search_fields = ('name', 'email', 'body')

class AllgroupsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline, userlistInline
        ]

admin.site.register(Allgroups, AllgroupsAdmin)
admin.site.register(Comment)
admin.site.register(userlist)
admin.site.register(Comment1, CommentAdmin)

