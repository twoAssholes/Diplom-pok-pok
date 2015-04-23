from django.forms import ModelForm
from polls.models import *

class QuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type', 'pub_date', 'pub_author', 'question_cost']



