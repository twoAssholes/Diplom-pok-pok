from django import forms



class QuestionsForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    question_type = forms.IntegerField()
    question_cost = forms.IntegerField()
    choice_text = forms.CharField(max_length=200)
    choice_cost_positive = forms.IntegerField()
    choice_cost_positive = forms.IntegerField()
    choice_cost_negative = forms.IntegerField()