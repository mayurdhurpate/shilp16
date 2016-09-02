from django.contrib import admin

from .models import *

class TeamInline(admin.TabularInline):
    model = Team.members.through
    extra = 0

class QUserAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]
    list_display = ('name', 'email', 'phone')

class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]
    list_display = ('name', 'slot')
    exclude = ['members',]

class HelpQuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'resolved')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'score')

admin.site.register(QUser, QUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(HelpQuestion, HelpQuestionAdmin)
admin.site.register(Question, QuestionAdmin)