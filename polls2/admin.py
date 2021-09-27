from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['text']}), 
        ("Date information", {'fields': ['pub_date']})
    )
    list_display = ['text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['text']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)