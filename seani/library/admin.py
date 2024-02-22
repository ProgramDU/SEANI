from django.contrib import admin

from .models import Module, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [ 'pk', 'question_text', 'module', 'correct']
    ordering = ['module']

#admin.site.register(Module)
#admin.site.register(Question, QuestionAdmin)
class QuestionInline(admin.StackedInline):
    model = Question

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_question']
    inlines = [QuestionInline]