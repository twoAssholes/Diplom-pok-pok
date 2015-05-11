# from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from polls.models import *
import json

input_dict = {
    1: 'radio',     #тип 1.2
    2: 'checkbox',  #тип 1.3
    3: 'radio',     #тип 1.1
}



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def make_context(amount=10):
    quest_list = []
    index = 0
    AllQuestion = Question.objects.all()[:amount]
    for quest in AllQuestion:
        ChoiceForQuestion = Choice.objects.filter(question=quest.pk)
        chois_list = []
        quest_dict = {}
        index += 1
        if ChoiceForQuestion:
            for chois in ChoiceForQuestion:
                chois_dict = {}
                chois_dict['choice_text'] = chois.choice_text
                chois_dict['choice_cost_positive'] = chois.choice_cost_positive
                chois_dict['choice_cost_negative'] = chois.choice_cost_negative
                chois_dict['choice_is_true'] = chois.choice_is_true
                chois_dict['choice_id'] = chois.id
                chois_list.append(chois_dict)
        quest_dict['question_text'] = quest.question_text
        quest_dict['question_choice'] = chois_list
        quest_dict['question_input_type'] = input_dict[quest.question_type]
        quest_dict['question_type'] = quest.question_type
        quest_dict['question_cost_positive'] = quest.question_cost_positive
        quest_dict['question_cost_negative'] = quest.question_cost_negative
        quest_dict['question_id'] = quest.id
        quest_dict['index'] = index
        quest_list.append(quest_dict)
    return quest_list

def make_context_js(amount=10):
    quest_list = []
    index = 0
    AllQuestion = Question.objects.all()[:amount]
    for quest in AllQuestion:
        ChoiceForQuestion = Choice.objects.filter(question=quest.pk)
        chois_list = []
        quest_dict = {}
        index += 1
        if ChoiceForQuestion:
            for chois in ChoiceForQuestion:
                chois_dict = {}
                chois_dict['choice_text'] = chois.choice_text
                chois_dict['choice_id'] = chois.id
                chois_list.append(chois_dict)
        quest_dict['question_text'] = quest.question_text
        quest_dict['question_choice'] = chois_list
        quest_dict['question_input_type'] = input_dict[quest.question_type]
        quest_dict['question_id'] = quest.id
        quest_dict['index'] = index
        quest_list.append(quest_dict)
    return quest_list


c = make_context()

c_js = make_context_js()


# def test(request):
#
#     return render_to_response('test.html', {
#         'formset': c_js,
#     })

#для jsona
def test(request):

    context_js = json.dumps(c_js, ensure_ascii=False)

    return render_to_response('jstext.html', {
        'formset': context_js,
    })


def vote(request):

    if request.method == 'POST':
        kwargs = [k for k in request.POST.lists()]
        keys_c = [k for k in request.POST.dict().keys()]
        BSum = 0 #Базовая оценка
        YSum = 0 #Продуктивная оценка
        for i in range(0, len(keys_c)):
            quest_id = keys_c[i]
            choice_list = request.POST.getlist(keys_c[i])
            for quest_index in c:
                if quest_index['question_id'] == int(keys_c[i]):
                    quest = quest_index
                    # quest['question_type'] = output_dict[quest['question_type']]
            asda = 'asd'
            # тип 1.2
            if quest['question_type'] == 1:
                BSum = BSum + max([v['choice_cost_positive'] for v in quest['question_choice']])
            else:
                BSum = BSum + 0

        return render_to_response("vote.html", {
            "vote": kwargs,
        })
