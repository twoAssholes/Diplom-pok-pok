# from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from polls.models import *
from polls.form import QuestionsForm

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:

        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def add(request):
    pass
    # pok = u'pok'
    # QuestionFormSet = modelformset_factory(Question)
    # if request.method == 'POST':
    #     formset = QuestionFormSet(request.POST, request.FILES)
    #     if formset.is_valid():
    #         formset.save()
    #         # do something.
    # else:
    #     formset = QuestionFormSet()
    # return render_to_response("add.html", {
    #     "formset": formset,
    # })
"""
Собрать лист словарей для каждой формы
{
    question_text = forms.CharField(max_length=200)
    question_type = forms.IntegerField()
    question_cost = forms.IntegerField()
    choice_text = forms.CharField(max_length=200)
    choice_cost_positive = forms.IntegerField()
    choice_cost_negative = forms.IntegerField()
}
после этого передать в набор форм, и вывести на экран
"""

def make_context():
    quest_list = []
    quest_dict = {}
    AllQuestion = Question.objects.all()
    for quest in AllQuestion:
        ChoiceForQuestion = Choice.objects.filter(question=quest.pk)
        chois_list = []
        if ChoiceForQuestion:
            for chois in ChoiceForQuestion:
                chois_list.append(chois.choice_text)
        quest_dict[quest.question_text] = chois_list
    return quest_dict


def test(request):
    c = [{'pok': 1, 'lok': 2}, {'pok': 'kaki', 'lok': 'drok'}]
    if request.method == 'POST':
        formset = QuestionFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = QuestionFormSet()
    return render_to_response("test.html", {
        "formset": c,
    })


