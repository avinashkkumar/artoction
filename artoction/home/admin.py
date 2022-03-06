from django.contrib import admin
from home.models import Feedback
# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user']

