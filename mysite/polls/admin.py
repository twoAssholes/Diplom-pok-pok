from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import *


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(User)