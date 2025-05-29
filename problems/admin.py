from django.contrib import admin
from  .models import Problem, TestCase

# Register your models here.

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('problem', 'id')
    list_filter = ('problem',)
    search_fields = ('problem__title',)
