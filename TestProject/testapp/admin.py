from django.contrib import admin
from testapp.models import Py_Question
# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','question_text','option_a','option_b','option_c','option_d','correct_answer','level','type']
admin.site.register(Py_Question,TestAdmin)
