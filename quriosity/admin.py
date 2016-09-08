from django.contrib import admin

from .models import *

class TeamInline(admin.TabularInline):
    model = Team.members.through
    extra = 0

class QuestionInline(admin.TabularInline):
    model = Slot.question.through
    extra = 0

class QUserAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'email']

class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]
    list_display = ('name', 'slot')
    exclude = ['members',]
    search_fields = ['name',]

class HelpQuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'resolved')
    search_fields = ['name', 'email']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]
    list_display = ('title', 'score')
    search_fields = ['title',]

class SlotAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('get_team', 'response', 'get_question')

    def get_team(self, obj):
        return obj.team.name

    def get_question(self, obj):
        return obj.question.title

admin.site.register(QUser, QUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(HelpQuestion, HelpQuestionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Response, ResponseAdmin)