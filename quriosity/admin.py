from django.contrib import admin

from .models import *

admin.site.register(QUser)
admin.site.register(Team)
admin.site.register(HelpQuestion)