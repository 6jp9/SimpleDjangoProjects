from django.db import models

# Create your models here.
class Py_Question(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)
    
    type = models.CharField(max_length=20)
    level = models.CharField(max_length=20)


    # def __str__(self):
    #     return self.question_text
 