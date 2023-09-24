from django.contrib import admin
from . models import *
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','short_details','user','add_time')
    search_fields = ('title','detail')

    def short_details(self, obj):
        return " ".join(obj.details.split()[:10]) + '...'
    short_details.short_description = 'Details'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','short_details','user','add_time')
    search_fields = ('details','question')

    def short_details(self, obj):
        return " ".join(obj.details.split()[:10]) + '...'
    short_details.short_description = 'Details'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('answer','details','user','add_time')
    search_fields = ('details','answer')




admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(Profile)