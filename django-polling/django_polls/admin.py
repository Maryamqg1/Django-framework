from django.contrib import admin
from .models import Question, Choice, Grade


# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(Grade)

admin.site.site_header = 'WELCOME TO THE DASHBOARD'
admin.site.site_title = 'CUSTOM INDEX'
admin.site.index_title = 'INDEX'

# class AuthorAdmin(admin.ModelAdmin):
#     pass
    #fields = ['question_text', 'pub_date', 'question', 'choice_text', 'votes',]
# admin.site.register(Question, AuthorAdmin)
# admin.site.register(Choice, AuthorAdmin)
# admin.site.register(Grade, AuthorAdmin)

# @admin.register(Question)
# class QAdmin (admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#     ordering = ['id']

# @admin.register(Choice)
# class CAdmin (admin.ModelAdmin):
#     exclude = ['votes']
    
@admin.register(Grade)
class GAdmin (admin.ModelAdmin):
    pass

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    # list_display = ["question_text", "pub_date"]
    search_fields = ["question_text"]
    list_filter = ["pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        ("QUESTION", {"fields": ["question_text"]}),
        ("DATE INFORMATION", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)