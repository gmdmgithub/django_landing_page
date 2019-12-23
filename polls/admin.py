from django.contrib import admin


# customizing admin site
admin.site.site_header = "System Admin"
admin.site.site_title = "System Admin Area"
admin.site.index_title = "Welcome to the Admin Area!"



# Register your models here.
from .models import Question, Choice

# Simple way just to have standard access to the data
# admin.site.register(Question)
# admin.site.register(Choice)


# More convenient when data are with relation

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [ 
                ('Question text', {'fielsd':['question_text']}),
                ('Date information', {'fielsd':['publish_date'], 'classes': ['collapse']}),
                ]
    
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)