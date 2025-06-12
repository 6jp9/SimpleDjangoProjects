from django.contrib import admin
from testapp.models import Question
# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','type','level','question_text','option_a','option_b','option_c','option_d','correct_answer']
admin.site.register(Question,TestAdmin)
