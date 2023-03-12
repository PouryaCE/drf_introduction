from django.contrib import admin
from .models import Person, Answer, Question
# Register your models here.
admin.site.register(Person)
admin.site.register(Answer)

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Question, QuestionAdmin)