from django.db import models
from problems.models import Problem

# Create your models here.
LANGUAGE_CHOICES = [
    {'python', 'Python'},
    {'cpp', 'C++'},
    {'java', 'Java'},
    ('c', 'C'),
]

class CodeSubmission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    code_file = models.FileField(upload_to='codes/')
    submitted_at = models.DateTimeField(auto_now_add=True)