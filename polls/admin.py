from django.contrib import admin

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