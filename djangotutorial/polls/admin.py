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

@admin.register(Question)
class QAdmin (admin.ModelAdmin):
    fields = ['question_text', 'pub_date']
    ordering = ['id']

@admin.register(Choice)
class CAdmin (admin.ModelAdmin):
    exclude = ['votes']
    
@admin.register(Grade)
class GAdmin (admin.ModelAdmin):
    pass