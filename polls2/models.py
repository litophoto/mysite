from django.db import models

from django import forms

from django.utils import timezone
import datetime

class Question(models.Model):
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Published date", default=timezone.now)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

ChoiceInlineForm = forms.inlineformset_factory(Question, Choice, fields=['text'], extra=3)